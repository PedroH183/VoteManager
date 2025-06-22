import datetime

from app.domain.entities.session_entity import Session


def test_session_is_open_and_not_closed():
    start = datetime.datetime.now() - datetime.timedelta(seconds=30)
    session = Session(topic_id=1, start_time=start, duration_minutes=1)
    assert session.is_open is True
    assert session.has_closed is False


def test_session_closed():
    start = datetime.datetime.now() - datetime.timedelta(minutes=5)
    session = Session(topic_id=1, start_time=start, duration_minutes=1)
    assert session.is_open is False
    assert session.has_closed is True
