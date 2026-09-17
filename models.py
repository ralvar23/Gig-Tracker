from pydantic import BaseModel
from typing import Optional

class SetlistCreate(BaseModel):
    name: str
    gig_date: Optional[str] = None
    location: Optional[str] = None
    notes: Optional[str] = None
    user_id: int


