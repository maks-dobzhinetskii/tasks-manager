import pytest

from django.contrib.auth.models import User
from django.utils import timezone

from tasks.models import Task
from users.models import CustomUser


@pytest.mark.django_db
def test_task_str(task):
    assert str(task) == "Test Task"


@pytest.mark.django_db
def test_task_absolute_url(task):
    assert task.get_absolute_url() == f"/tasks/{task.id}/"


@pytest.mark.django_db
def test_task_is_completed_default(task):
    assert not task.is_completed


@pytest.mark.django_db
def test_task_draft_default(task):
    assert not task.draft


@pytest.mark.django_db
def test_task_draft_true():
    user = CustomUser.objects.create_user(username="testuser", password="testpass")
    draft_task = Task.objects.create(
        title="Test Draft Task",
        body="This is a test draft task",
        created_at=timezone.now(),
        author=user,
        draft=True,
    )
    assert draft_task.draft
