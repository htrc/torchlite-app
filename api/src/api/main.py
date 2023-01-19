import uuid
import json
from api import torchlite
import logging
from fastapi import FastAPI, HTTPException
from api.extracted_features import WorkSet
from api.dashboard import Dashboard
from api.torchlite import TorchLite
from api.widgets import WidgetFactory

torchlite = TorchLite()
torchlite.add_workset(
    WorkSet(
        url='https://worksets.htrc.illinois.edu/wsid/771d1500-7ac6-11eb-8593-e5f5ab8b1c01'
    )
)

mini_workset = WorkSet()
[
    mini_workset.add_volume(v_id)
    for v_id in ["uc1.32106011187561", "mdp.35112103187797", "uc1.$b684263"]
]
mini_workset.description = "minimal workset"
torchlite.add_workset(mini_workset)


torchlite.add_dashboard(Dashboard())


app = FastAPI()


@app.get("/")
def read_root():
    return {"sample_worksets": [w.description for w in torchlite.worksets.values()]}


@app.get("/dashboards")
def get_root_dashboard():
    return [{k: v} for k, v in torchlite.dashboards.items()]


@app.get("/dashboards/{id}")
async def get_dashboard(id: str):
    try:
        d = torchlite.get_dashboard(id)
        return d
    except KeyError:
        raise HTTPException(status_code=404, detail="dashboard not found")


@app.post("/dashboards")
def create_dashboard():
    d = Dashboard()
    torchlite.add_dashboard(d)
    return d.id


@app.get("/dashboards/{dashboard_id}/workset")
def get_dashboard_workset(dashboard_id: str):
    dashboard = torchlite.get_dashboard(dashboard_id)
    return dashboard.workset


@app.put("/dashboards/{dashboard_id}/workset/{workset_id}")
def put_dashboard_workset(dashboard_id: str, workset_id: str):
    dashboard = torchlite.get_dashboard(dashboard_id)
    workset = torchlite.get_workset(workset_id)
    dashboard.workset = workset
    return dashboard.workset


@app.get("/dashboards/{dashboard_id}/widgets")
def get_dashboard_widgets(dashboard_id: str):
    dashboard = torchlite.get_dashboard(dashboard_id)
    return dashboard.widgets


@app.post("/dashboards/{dashboard_id}/widgets/{widget_type}")
def post_dashboard_widget(dashboard_id: str, widget_type: str):
    db = torchlite.get_dashboard(dashboard_id)
    widget = WidgetFactory.make_widget('MetadataWidget', db.workset)
    db.add_widget(widget)


##########
# WorkSets
##########
@app.get("/worksets")
def get_worksets():
    worksets = [{k: v.description} for k, v in torchlite.worksets.items()]
    return worksets
