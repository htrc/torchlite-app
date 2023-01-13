import uuid
import json
import requests
import logging
from fastapi import FastAPI, HTTPException
from extracted_features import WorkSet
from dashboard import Dashboard


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


sample_ws_ids = [
    'https://worksets.htrc.illinois.edu/wsid/771d1500-7ac6-11eb-8593-e5f5ab8b1c01'
]

sample_worksets = []
for id in sample_ws_ids:
    w = WorkSet(id)
    sample_worksets.append(w)

mini_workset = WorkSet()

mini_workset.volumes = "uc1.32106011187561"
mini_workset.volumes = "mdp.35112103187797"
mini_workset.volumes = "uc1.$b684263"
mini_workset.description = "minimal workset"

sample_worksets.append(mini_workset)


app = FastAPI()


dashboards = {}

d = Dashboard()
dashboards[d.id] = d


@app.get("/")
def read_root():
    return {
        "sample_worksets": [w.description for w in sample_worksets],
    }


@app.get("/dashboards")
def get_root_dashboard():
    return [{k: v} for k, v in dashboards.items()]


@app.get("/dashboards/{id}")
async def get_dashboard(id: str):
    try:
        d = dashboards[id]
        return d
    except KeyError:
        raise HTTPException(status_code=404, detail="dashboard not found")


@app.post("/dashboard")
def create_dashboard():
    d = Dashboard()
    dashboards[d.id] = d
    return d.id


##########
# WorkSets
##########
