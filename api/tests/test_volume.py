import pytest
from api.extracted_features import Volume


@pytest.fixture
def volume():
    v = Volume("uc1.32106011187561")
    return v


def test_title(volume):
    assert volume.title == "Bilder vom Erzählen : Gedichte /"


def test_type(volume):
    assert 'Book' in volume.type
