import pytest
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE
from model_bakery import baker

from . import create_logentry


@pytest.mark.django_db
def test_create_logentry():
    user1 = baker.make('User')
    user2 = baker.make('User')

    assert not LogEntry.objects.all()

    create_logentry(creator=user1, object=user2)

    assert LogEntry.objects.all()
    logentry = LogEntry.objects.get(
        user=user1, object_id=user2.id, object_repr=str(user2), action_flag=ADDITION)
    assert logentry.change_message == '添加'

    create_logentry(creator=user1, object=user2, is_change=True, message='测试')
    logentry = LogEntry.objects.get(
        user=user1, object_id=user2.id, object_repr=str(user2), action_flag=CHANGE)
    assert logentry.change_message == '测试'
