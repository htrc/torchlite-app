from api.extracted_features import WorkSet
from api.dashboard import Dashboard


class TorchLite:
    def __init__(self):
        self._dashboards = {}
        self._widgets = {}
        self._worksets = {}

    @property
    def dashboards(self):
        return self._dashboards

    def add_dashboard(self, dashboard):
        self._dashboards[str(dashboard.id)] = dashboard
        return self.dashboards

    def get_dashboard(self, dashboard_id):
        return self._dashboards[dashboard_id]

    def delete_dashboard(self, dashboard_id):
        del self._dashboards[dashboard_id]
        return self.dashboards

    @property
    def widgets(self):
        return self._widgets

    def add_widget(self, widget):
        self.widgets[str(widget.id)] = widget
        return self.widgets

    def get_widget(self, widget_id):
        return self.widgets[widget_id]

    def delete_widget(self, widget_id):
        del self.widgets[widget_id]
        return self.widgets

    @property
    def worksets(self):
        return self._worksets

    def add_workset(self, workset):
        self.worksets[str(workset.id)] = workset
        return self.worksets

    def get_workset(self, workset_id):
        return self.worksets[workset_id]

    def delete_workset(self, workset_id):
        del self.worksets[workset_id]
        return self.worksets