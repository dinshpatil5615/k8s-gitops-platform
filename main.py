from fastapi import FastAPI
app = FastAPI(title = "Internal platform Demo App")

@app.get("/")
def home():
    return {"message":"Welcome to internal Developer Platform"}

@app.get("/health")
def home():
    return {"Status":"UP"}

@app.get("/version")
def home():
    return {"version":"v1.0.0"}