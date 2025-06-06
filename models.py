# models.py
from typing import Optional, List
from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from datetime import datetime

class Club(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    username: str
    password_hash: str

class Venue(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    club_id: int

class DayPass(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    club_id: int
    club_name: str
    timestamp: datetime

class Result(BaseModel):
    timestamp: str
    club_id: int
    venue_name: str
    status: str
    message1: str
    message2: str
    track_condition: str
    correct_weight: str
    raw_message: str
    runners: Optional[List[str]] = None

    class Config:
        extra = "allow"
