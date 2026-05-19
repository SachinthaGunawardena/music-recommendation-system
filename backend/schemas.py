# backend/schemas.py

from pydantic import BaseModel

class SongResponse(BaseModel):
    track_name: str
    artist_name: str
    genre: str