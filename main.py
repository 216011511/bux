from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

from app.features.artist_registration import route
app.include_router(route.router)

from app.features.album_registration import route
app.include_router(route.router)

from app.features.song_registration import route
app.include_router(route.router)

@app.get("/")
async def root():
    return {"message": "Authentication Backend Application"}