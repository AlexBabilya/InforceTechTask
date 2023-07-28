import pytest

from modules.fixtures.user import user
from modules.restaurant.models import Restaurant


@pytest.mark.django_db
def test_create_restaurant(user):
    data_restaurant = {
        "name": "pytest",
        "address": "pytest",
        "created_by": user.username,
    }
    restaurant = Restaurant.objects.create(**data_restaurant)
    assert restaurant.name == data_restaurant["name"]
    assert restaurant.address == data_restaurant["address"]
    assert restaurant.created_by == data_restaurant["created_by"]
