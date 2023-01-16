import pytest
from api.dashboard import Dashboard
from api.extracted_features import WorkSet, Volume
from api.widgets import WidgetFactory


@pytest.fixture
def workset():
    ws = WorkSet()
    ws.add_volume("loc.ark+=13960=t46q23w14")
    return ws


@pytest.fixture
def widget(workset):
    w = WidgetFactory.make_widget('MetadataWidget', workset)
    return w


def test_dashboard(workset, widget):
    dashboard = Dashboard()
    assert dashboard.widgets == {}
    dashboard.add_widget(widget)
    assert dashboard.widgets[str(widget.id)] == widget
