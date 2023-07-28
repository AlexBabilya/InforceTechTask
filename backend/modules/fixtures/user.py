import pytest
from modules.user.models import User

@pytest.fixture
def user(db) -> User:
    data_user = {
            "username": "pytest",
            "email": "pytest@gmail.com",
            "first_name": "pytest",
            "last_name": "pytest",
            "phone": "+2404554444",
            "identification_no": "5343434242",
            "password": "1234567"
        }
    return User.objects.create_user(**data_user)