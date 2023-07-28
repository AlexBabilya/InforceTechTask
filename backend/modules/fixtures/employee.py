import pytest

from modules.employee.models import Employee
from modules.fixtures.user import user

@pytest.fixture
def employee(db, user)  -> Employee:
    data_employee = {
            "user": user,
    }
    return Employee.objects.create_user(**data_employee)