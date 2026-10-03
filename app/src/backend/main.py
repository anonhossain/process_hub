from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from spotify_music_downloader.spotify_views import api


app = FastAPI(
    title="Process Hub",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="10.10.29.164",
        port=8080
    )