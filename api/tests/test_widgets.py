import pytest
from api.extracted_features import WorkSet
from api.widgets import Widget, MetadataWidget
import json


@pytest.fixture
def workset():
    mini_workset = WorkSet()

    mini_workset.volumes = "uc1.32106011187561"
    mini_workset.volumes = "mdp.35112103187797"
    mini_workset.volumes = "uc1.$b684263"
    mini_workset.description = "minimal workset"
    return mini_workset


def test_widget(workset):
    w = Widget(workset)
    assert w._data == None
    assert w.data == []


def test_metadata_widget(workset):
    w = MetadataWidget(workset)
    assert len(w.data) == 3
