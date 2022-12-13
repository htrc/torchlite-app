import uuid
import json
import requests
import logging
from fastapi import FastAPI, HTTPException
from extracted_features import WorkSet
from dashboard import Dashboard

sample_ws_ids = [
    'https://worksets.htrc.illinois.edu/wsid/771d1500-7ac6-11eb-8593-e5f5ab8b1c01'
]

sample_worksets = []
for id in sample_ws_ids:
    w = WorkSet([])
    w.import_ws(id)
    sample_worksets.append(w)

app = FastAPI()

workset = WorkSet(["uc1.32106011187561", "mdp.35112103187797", "uc1.$b684263"])
workset.description = "minimal workset"

sample_worksets.append(workset)

dashboards = {}

d = Dashboard()
dashboards[d.id] = d


@app.get("/")
def read_root():
    return {
        "sample_worksets": [w.description for w in sample_worksets],
    }


@app.get("/dashboard")
def get_root_dashboard():
    return [{k: v} for k, v in dashboards.items()]


@app.get("/dashboard/{id}")
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
