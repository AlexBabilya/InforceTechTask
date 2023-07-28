import pytest

from modules.menu.models import Menu
from .user import user
from .restaurant import restaurant


@pytest.fixture
def menu(db, user, restaurant) -> Menu:
    data_menu = {
        "restaurant": restaurant,
        "file": "pytest.txt",
        "uploaded_by": user.username,
        "votes": 0,
    }
    return Menu.objects.create(**data_menu)
