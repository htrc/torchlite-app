import pytest
from api.torchlite import TorchLite
from api.dashboard import Dashboard
from api.extracted_features import Volume, WorkSet
from api.widgets import WidgetFactory


@pytest.fixture
def volume_1():
    v = Volume("uc1.32106011187561")
    return v


@pytest.fixture
def volume_2():
    return Volume("loc.ark+=13960=t46q23w14")


@pytest.fixture
def workset_1(volume_1, volume_2):
    ws = WorkSet()
    ws.volumes = volume_1
    ws.volumes = volume_2
    return ws


@pytest.fixture
def widget_1(workset_1):
    return WidgetFactory.make_widget('MetadataWidget', workset_1)


def test_dashboards():
    torchlite = TorchLite()
    assert torchlite.dashboards == {}
    d = Dashboard()
    torchlite.add_dashboard(d)
    assert torchlite.dashboards[d.id] == d
    assert torchlite.get_dashboard(d.id) == d
    assert len(torchlite.dashboards) == 1
    torchlite.delete_dashboard(d.id)
    assert len(torchlite.dashboards) == 0
