from pydantic import BaseModel
from typing import Optional

class SetlistCreate(BaseModel):
    name: str
    gig_date: Optional[str] = None
    location: Optional[str] = None
    notes: Optional[str] = None
    user_id: int

class SongCreate(BaseModel):
    title: str
    artist: Optional[str] = None
    lyrics: Optional[str] = None
    key: Optional[str] = None
    tempo: Optional[int] = None
    duration_seconds: Optional[int] = None
    genre: Optional[str] = None
    energy_level: Optional[int] = None
    last_played_date: Optional[str] = None
    crowd_response_rating: Optional[str] = None
    difficulty: Optional[int] = None
    tags: Optional[str] = None
    metadata_verified: bool = False
