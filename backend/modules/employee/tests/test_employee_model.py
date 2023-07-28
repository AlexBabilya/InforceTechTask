import pytest

from modules.fixtures.user import user
from modules.employee.models import Employee


@pytest.mark.django_db
def test_create_employee(user):
    data_employee = {
        "user": user,
    }
    employee = Employee.objects.create(created_by=user.username, **data_employee)
    assert employee.user == data_employee["user"]
