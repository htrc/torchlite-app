from typing import Union
from fastapi import FastAPI
from extracted_features import WorkSet

app = FastAPI()

workset = WorkSet(["uc1.32106011187561", "mdp.35112103187797", "uc1.$b684263"])


@app.get("/")
def read_root():
    return {"hello": "world", "volumes": workset.volumes}
