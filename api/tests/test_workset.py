import pytest
from api.extracted_features import WorkSet, Page


@pytest.fixture
def workset():
    return WorkSet(["uc1.32106011187561", "mdp.35112103187797", "uc1.$b684263"])


def test_volumes(workset):
    assert len(workset.volumes) == 3


def test_tokens(workset):
    assert len(workset.tokens) == 47892

def test_import():
    ws_id = 'https://worksets.htrc.illinois.edu/wsid/771d1500-7ac6-11eb-8593-e5f5ab8b1c01'
    workset = WorkSet()
    workset.import_ws(ws_id)
    assert len(workset.volumes) == 16
