import pytest
from modules.role.models import Role


@pytest.mark.django_db
def test_create_role():
    data_role = {
            "name": "Chef",
    }
    role = Role.objects.create(**data_role)
    assert role.name == data_role["name"]
    