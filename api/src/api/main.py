import uuid
import json
from typing import Union
from fastapi import FastAPI, HTTPException
from extracted_features import WorkSet
from dashboard import Dashboard


app = FastAPI()

workset = WorkSet(["uc1.32106011187561", "mdp.35112103187797", "uc1.$b684263"])

dashboards = {}

d = Dashboard()
dashboards[d.id] = d


@app.get("/")
def read_root():
    return {"hello": "world", "volumes": workset.volumes}


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
