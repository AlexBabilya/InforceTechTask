import pytest

from modules.fixtures.restaurant import restaurant
from modules.fixtures.user import user
from modules.menu.models import Menu


@pytest.mark.django_db
def test_create_menu(restaurant, user):
    data_menu = {
            "restaurant": restaurant,
            "file": "pytest.txt",
            "uploaded_by": user.username,
            "votes": 0,
    }
    menu = Menu.objects.create(**data_menu)
    assert menu.restaurant == data_menu["restaurant"]
    assert menu.file == data_menu["file"]
    assert menu.uploaded_by == data_menu["uploaded_by"]
    assert menu.votes == data_menu["votes"]

