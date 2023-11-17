from fastapi import FastAPI

from helper.model import fielder

app = FastAPI(title="Model Intra")

@app.get("/")
def root():
    return {"msg":"Hallo !"}

@app.post("/model_perform")
def perform(sentence : str):
    result = fielder(sentence)
    return {"result":result}