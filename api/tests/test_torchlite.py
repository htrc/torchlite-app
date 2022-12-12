import pytest
from api.extracted_features import Volume


@pytest.fixture
def volume_1():
    return Volume("loc.ark+=13960=t46q23w14")


@pytest.fixture
def page_1(volume_1):
    return volume_1.pages[0]


def test_volume(volume_1):
    assert volume_1.id == "loc.ark+=13960=t46q23w14"


def test_page(page_1):
    assert page_1.tokenCount == 52


def test_volume_tokens(volume_1):
    tokens = volume_1.tokens
    assert len(tokens) == 1053
