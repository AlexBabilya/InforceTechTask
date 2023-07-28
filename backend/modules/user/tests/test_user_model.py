import pytest
from modules.user.models import User


@pytest.mark.django_db
def test_create_user():
    data_user = {
        "email": "pytest@gmail.com ",
        "first_name": "pytest",
        "last_name": "pytest",
        "phone": "+2404554444",
        "identification_no": "5343434242",
    }
    user = User.objects.create(**data_user)
    assert user.email == data_user["email"]
    assert user.first_name == data_user["first_name"]
    assert user.last_name == data_user["last_name"]
    assert user.phone == data_user["phone"]
    assert user.identification_no == data_user["identification_no"]


@pytest.mark.django_db
def test_create_superuser():
    data_user = {
        "username": "pytest",
        "email": "pytest@gmail.com",
        "first_name": "pytest",
        "last_name": "pytest",
        "phone": "+2404554444",
        "identification_no": "5343434242",
    }
    user = User.objects.create_superuser(**data_user)
    assert user.email == data_user["email"]
    assert user.first_name == data_user["first_name"]
    assert user.last_name == data_user["last_name"]
    assert user.phone == data_user["phone"]
    assert user.identification_no == data_user["identification_no"]
    assert user.is_superuser == True
    assert user.is_staff == True
