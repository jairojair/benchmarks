from fastapi import FastAPI

app = FastAPI()

@app.get("/fastapi")
def home():
    return {"Hello": "fastapi!"}