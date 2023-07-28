import pytest
from modules.restaurant.models import Restaurant

from .user import user


@pytest.fixture
def restaurant(db, user) -> Restaurant:
    data_restaurant = {
        "name": "pytest",
        "address": "pytest",
        "created_by": user.username,
    }
    return Restaurant.objects.create(**data_restaurant)
