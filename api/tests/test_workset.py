import pytest
from extracted_features.workset import WorkSet
from extracted_features.page import Page


@pytest.fixture
def workset():
    return WorkSet(["uc1.32106011187561", "mdp.35112103187797", "uc1.$b684263"])


def test_volumes(workset):
    assert len(workset.volumes) == 3


def test_tokens(workset):
    assert len(workset.tokens) == 47892