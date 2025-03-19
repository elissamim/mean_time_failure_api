from fastapi import FastAPI
from pydantic import BaseModel

import pandas as pd


app = FastAPI()

class InputData(BaseModel):
    path: str
    start_date: str
    end_date: str

def count_failures(path:str,
                  start_date:str,
                  end_date:str) -> dict:

    df = pd.read_csv(path)
    df["timestamp"]=pd.to_datetime(df["timestamp"], format = "%Y-%m-%d %H-%M-%S")
    df = (
        df[(df["timestamp"]>=start_date)&(df["timestamp"]<=end_date)]
    )
    df = df[df["event_type"]=="Failure"]
    result = (
        df.groupby("equipment_id")["timestamp"].apply(lambda x: x.sort_values().diff().mean())
    )
    result = result.dropna().dt.total_seconds().to_dict()
    return result

@app.post("/predict")
def predict(input_data:InputData):
    
    result = count_failures(input_data.path,
                            input_data.start_date,
                            input_data.end_date)
    
    return result