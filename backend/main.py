from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from .database import create_lead, init_db

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database
init_db()

# Pydantic model for lead data
class LeadBase(BaseModel):
    name: str
    phone: str
    email: str

@app.post("/api/leads")
async def submit_lead(lead: LeadBase):
    try:
        create_lead(lead.name, lead.phone, lead.email)
        return {"message": "Lead submitted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Mount static files (frontend)
app.mount("/", StaticFiles(directory="frontend", html=True), name="static")
