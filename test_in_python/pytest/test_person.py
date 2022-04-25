from person import Person 
import pytest

@pytest.fixture
def person():
    return Person("matin", "sajadi", 21, "yazd")


def test_full_name(person):
    assert isinstance(person.full_name(), str)

def test_locat(person):
    assert isinstance(person.locat(), str)


def test_email_person(person):
    assert isinstance(person.email_person(), str)
