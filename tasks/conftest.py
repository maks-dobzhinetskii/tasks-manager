import pytest

from django.utils import timezone

from tasks.models import Task
from users.models import CustomUser


@pytest.fixture()
def user():
    return CustomUser.objects.create_user(username="testuser", password="testpass")


@pytest.fixture()
def task(user):
    return Task.objects.create(
        title="Test Task",
        body="This is a test task",
        created_at=timezone.now(),
        author=user,
    )
