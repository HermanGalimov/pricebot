from fastapi import FastAPI
from app import db, models, scheduler

app = FastAPI(title="PriceWatcherBot")

@app.on_event("startup")
async def startup_event():
    db.init_db()
    scheduler.start()

@app.get("/")
async def root():
    return {"message": "PriceWatcherBot is running"}
