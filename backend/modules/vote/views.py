from django.db.models import Q
from django.db.models import Max
from django.db import connection
from django.db.models import F, Window
from django.db.models.functions import Rank
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from datetime import datetime
from datetime import date, timedelta

from modules.auth.handlers import jwt_decode_handler
from modules.menu.models import Menu
from modules.menu.serializers import MenuResultListSerializer
from modules.vote.models import Vote

todays_date = settings.CURRENT_DATE.date()


class VoteAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, menu_id):
        username = jwt_decode_handler(request.auth).get('username')
        todays_date = settings.CURRENT_DATE.date()

        menu = Menu.objects.get(id=menu_id)

        if Vote.objects.filter(
                employee__user__username=username,
                voted_at__date=todays_date,
                menu__id=menu_id
            ).exists():
            
            res = {
                "msg": 'You already voted!', 
                "data": None, 
                "success": False
            }
            return Response(data=res, status=status.HTTP_200_OK)
        else:
            menu.votes += 1
            menu.save()

            qs = Menu.objects.filter(Q(created_at__date=todays_date))
            serializer = MenuResultListSerializer(qs, many=True)
            res = {
                "msg": 'You voted successfully!',
                "data": serializer.data,
                "success": True
            }
            return Response(data=res, status=status.HTTP_200_OK)


class ResultsAPIView(APIView):
    def get(self, request):

        today = date.today()
        start = today - timedelta(days=today.weekday())

        current_menu_qs = Menu.objects.filter(
            Q(created_at__date=todays_date)).order_by('-votes')

        if len(current_menu_qs) == 0:
            res = {
                "msg": 'Results not found! no menus found for today.',
                "data": None,
                "success": False
            }
            return Response(data=res, status=status.HTTP_200_OK)

        # Populate menu list from monday to today.
        consecutive_list = Menu.objects.filter(created_at__gte=start).extra(select={
                'day': connection.ops.date_trunc_sql(
                    'day',
                    'created_at'
                    )
                }).values('day', 'id').annotate(max_vote=Max('votes'))

        # populate consecutive Days
        date_strs = [str(date.get('day')) for date in consecutive_list]

        dates = [datetime.strptime(d, "%Y-%m-%d %H:%M:%S") for d in date_strs]

        date_ints = set([d.toordinal() for d in dates])

        if len(date_ints) == 1:
            # If all unique
            new_queryset = Menu.objects.filter(
                created_at__date=todays_date).annotate(
                rank=Window(
                    expression=Rank(),
                    order_by=F('votes').desc(),
                )
            )

            result = [{"rank": item.rank,
                       "restaurant": item.restaurant.name,
                       "votes": item.votes} for item in new_queryset]

            res = {
                "msg": 'success', 
                "data": result, 
                "success": True
            }
            return Response(data=res, status=status.HTTP_200_OK)

        elif max(date_ints) - min(date_ints) == 3:
            # If consecutive winner found 3 times
            list_ = [item for item in consecutive_list if str(item.get(
                'day'))[:10] == str(todays_date)]
            current_max = list_[0]
            current_max_pk = current_max.get('id')
            new_current_list = [
                item.id for item in current_menu_qs
                if item.id != current_max_pk]

            new_queryset = Menu.objects.filter(id__in=new_current_list
                                               ).annotate(
                rank=Window(
                    expression=Rank(),
                    order_by=F('votes').desc(),
                )
            )

            result = [
                {
                    "rank": item.rank,
                    "votes": item.votes,
                    "restaurant": item.restaurant.name
                }
                for item in new_queryset
            ]

            res = {
                "msg": 'success', 
                "data": result, 
                "success": True
            }
            return Response(data=res, status=status.HTTP_200_OK)

        else:
            new_queryset = Menu.objects.filter(
                created_at__date=todays_date
            ).annotate(
                rank=Window(
                    expression=Rank(),
                    order_by=F('votes').desc(),
                )
            )

            result = [{"rank": item.rank,
                       "votes": item.votes,
                       "restaurant": item.restaurant.name,
                       "file": item.file.url} for item in new_queryset]

            res = {
                "msg": 'success', 
                "data": result, 
                "success": True
            }
            return Response(data=res, status=status.HTTP_200_OK)