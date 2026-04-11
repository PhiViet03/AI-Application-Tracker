from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, String, Date, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
import uvicorn

# DB setup
DATABASE_URL = "sqlite:///./AppDatabase.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# Table model
class AppList(Base):
    __tablename__ = "AppList"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    DateApplied = Column(Date)

# Create table
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI()

# Request body schema
class Application(BaseModel):
    name: str
    DateApplied: date

@app.post("/application")
def application_sent(app_data: Application):
    db = SessionLocal()

    new_entry = AppList(
        name=app_data.name,
        DateApplied=app_data.DateApplied
    )

    db.add(new_entry)
    db.commit()
    db.close()

    return {"message": "Saved successfully"}

@app.get("/applications")
def get_applications():
    db = SessionLocal()
    apps = db.query(AppList).all()
    db.close()
    return apps

if __name__ == "__main__": 
    uvicorn.run(app, host="0.0.0.0", port=8000)