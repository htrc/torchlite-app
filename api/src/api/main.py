import uuid
import json
from api import torchlite
import logging
from fastapi import FastAPI, HTTPException
from api.extracted_features import WorkSet
from api.dashboard import Dashboard
from api.torchlite import TorchLite


torchlite = TorchLite()

sample_ws_ids = []

torchlite.add_workset(
    WorkSet(
        'https://worksets.htrc.illinois.edu/wsid/771d1500-7ac6-11eb-8593-e5f5ab8b1c01'
    )
)

mini_workset = WorkSet()
[
    mini_workset.add_volume(v_id)
    for v_id in ["uc1.32106011187561", "mdp.35112103187797", "uc1.$b684263"]
]

mini_workset.description = "minimal workset"

torchlite.add_widget(mini_workset)

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
        d = torchlite.dashboards[id]
        return d
    except KeyError:
        raise HTTPException(status_code=404, detail="dashboard not found")


@app.post("/dashboard")
def create_dashboard():
    d = Dashboard()
    torchlite.add_dashboard(d)
    return d.id


##########
# WorkSets
##########
