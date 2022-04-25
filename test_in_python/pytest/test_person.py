from person import Person

import pytest

@pytest.fixture
def person():
    return Person('sina','nazem','male',2000)


def test_full_name(person):
    assert isinstance(person.full_name(),str)



def test_age(person):
    assert isinstance(person.age(),int)


def test_generate_email(person):
    assert isinstance(person.generate_email(),str)
