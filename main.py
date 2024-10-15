from fastapi import FastAPI, HTTPException, Header, Response
import pandas as pd

app = FastAPI()

apiKey = "secret123"
@app.get("/")
def root():
    return{"messag": "HelloWorld!"}

@app.get("/protected")
def root(key: str = Header(None)):
    if key == None or key != apiKey:
        raise HTTPException(status_code=401, detail="Ivalid API key!")
    
    df = pd.read_csv('data_aja.csv')

    return {
        "data": df.to_dict(orient="records"),
        "Header": Response(content="ini Header").headers }

@app.get("/detail/{id}")
def root(id: int):
    df = pd.read_csv('data_aja.csv')

    filter = df[df.id == id]

    if len(filter) == 0:
        raise HTTPException(status_code=404, detail="data tidak ditemukan")
    else:
        return filter.to_dict(orient="records")

    