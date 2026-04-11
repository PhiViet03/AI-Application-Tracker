from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict
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
    Company = Column(String, nullable = False)
    Role = Column(String)
    Date_Applied = Column(Date, nullable = False)
    Status = Column(String, default="applied")

# Create table
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI()

# Request body schema
class Application(BaseModel):
    Company: str
    Role: str
    Date_Applied: date
    Status: str = "applied"

class ApplicationResponse(BaseModel):
    id: int
    Company: str
    Role: str
    Date_Applied: date
    Status: str

    model_config = ConfigDict(from_attributes=True)

# Routes
@app.post("/application")
def application_sent(app_data: Application):
    db = SessionLocal()

    new_entry = AppList(
        Company=app_data.Company,
        Role=app_data.Role,
        Date_Applied=app_data.Date_Applied,
        Status=app_data.Status
    )

    db.add(new_entry)
    db.commit()
    db.close()
    db.refresh(new_entry)

    return new_entry

@app.get("/applications", response_model=list[ApplicationResponse])
def get_applications():
    db = SessionLocal()
    apps = db.query(AppList).all()
    db.close()
    return apps

@app.put("/update_status/{app_id}")
def update_status(app_id: int, new_status: str):
    db = SessionLocal()
    db_id = db.query(AppList).filter(AppList.id == app_id).first()

    if db_id is None:
        db.close()
        raise HTTPException(status_code=404, detail="Application not found")
    
    db_id.Status = new_status
    db.commit()
    db.close()

    return {"message": "Status updated successfully"}

@app.delete("/delete_application/{app_id}")
def delete_application(app_id: int):
    db = SessionLocal()
    db_id = db.query(AppList).filter(AppList.id == app_id).first()

    if db_id is None:
        db.close()
        raise HTTPException(status_code=404, detail="Application not found")
    
    db.delete(db_id)
    db.commit()
    db.close()

    return {"message": "Application deleted successfully"}
        
if __name__ == "__main__": 
    uvicorn.run(app, host="0.0.0.0", port=8000)