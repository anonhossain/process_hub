# from typing import Literal
# from pydantic import BaseModel, Field


# class Spotify_Downloader(BaseModel):

#     playlist_url: str = Field(
#         ...,
#         description="URL of the Spotify playlist to download"
#     )

#     output_dir: str = Field(
#         default=r"app\output",
#         description="Directory where downloaded files will be saved"
#     )

#     audio_format: Literal["mp3", "flac", "wav", "m4a"] = Field(
#         default="m4a",
#         description="Desired audio format"
#     )

#     bitrate: Literal["128k", "192k", "256k", "320k"] = Field(
#         default="256k",
#         description="Audio bitrate"
#     )


from typing import Literal
from pydantic import BaseModel, Field


class Spotify_Downloader(BaseModel):

    playlist_url: str = Field(
        ...,
        description="URL of the Spotify playlist to download"
    )

    audio_format: Literal["mp3", "flac", "wav", "m4a"] = Field(
        default="m4a",
        description="Desired audio format"
    )

    bitrate: Literal["128k", "192k", "256k", "320k"] = Field(
        default="256k",
        description="Audio bitrate"
    )