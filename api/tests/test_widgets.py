import pytest
from api.extracted_features import WorkSet
from api.widgets import Widget, MetadataWidget
import json


@pytest.fixture
def workset():
    return WorkSet(["uc1.32106011187561", "mdp.35112103187797", "uc1.$b684263"])


def test_widget(workset):
    w = Widget(workset)
    assert w._data == None
    assert w.data == []


def test_metadata_widget(workset):
    w = MetadataWidget(workset)
    assert w.data == ["foo"]
