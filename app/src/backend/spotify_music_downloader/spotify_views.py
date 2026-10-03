# from fastapi import APIRouter

# from .model import Spotify_Downloader
# from .spotify_downloader import download_playlist


# api = APIRouter()


# @api.post(
#     "/download_playlist",
#     response_model=dict,
#     summary="Download Spotify playlist",
#     tags=["Spotify_Downloader"]
# )
# async def download_spotify_playlist(payload: Spotify_Downloader):

#     try:
#         download_playlist(
#             playlist_url=payload.playlist_url,
#             output_dir=payload.output_dir,
#             audio_format=payload.audio_format,
#             bitrate=payload.bitrate
#         )

#         return {
#             "status": "success",
#             "message": "Playlist downloaded successfully"
#         }

#     except Exception as e:
#         return {
#             "status": "error",
#             "message": str(e)
#         }


# import os
# import shutil
# import tempfile

# from fastapi import APIRouter, BackgroundTasks, HTTPException
# from fastapi.responses import FileResponse

# from .model import Spotify_Downloader
# from .spotify_downloader import download_playlist


# api = APIRouter()


# @api.post(
#     "/download_playlist",
#     summary="Download Spotify playlist",
#     tags=["Spotify_Downloader"]
# )
# async def download_spotify_playlist(
#     payload: Spotify_Downloader,
#     background_tasks: BackgroundTasks
# ):

#     # Create temporary directory
#     temp_dir = tempfile.mkdtemp()

#     try:
#         download_playlist(
#             playlist_url=payload.playlist_url,
#             output_dir=temp_dir,
#             audio_format=payload.audio_format,
#             bitrate=payload.bitrate
#         )

#         # ZIP all downloaded songs
#         zip_path = shutil.make_archive(
#             base_name=temp_dir,
#             format="zip",
#             root_dir=temp_dir
#         )

#         # Delete temporary files after response finishes
#         background_tasks.add_task(
#             shutil.rmtree,
#             temp_dir,
#             ignore_errors=True
#         )

#         background_tasks.add_task(
#             os.remove,
#             zip_path
#         )

#         return FileResponse(
#             path=zip_path,
#             media_type="application/zip",
#             filename="spotify_playlist.zip",
#             background=background_tasks
#         )

#     except Exception as e:

#         shutil.rmtree(
#             temp_dir,
#             ignore_errors=True
#         )

#         raise HTTPException(
#             status_code=500,
#             detail=str(e)
#         )


import os
import shutil
import tempfile
import traceback

from fastapi import APIRouter, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse

from .model import Spotify_Downloader
from .spotify_downloader import download_playlist


api = APIRouter()


@api.post(
    "/download_playlist",
    summary="Download Spotify playlist",
    tags=["Spotify_Downloader"]
)
async def download_spotify_playlist(
    payload: Spotify_Downloader,
    background_tasks: BackgroundTasks
):

    temp_dir = tempfile.mkdtemp()

    print("\n==============================")
    print("TEMP DIRECTORY:", temp_dir)
    print("PLAYLIST:", payload.playlist_url)
    print("FORMAT:", payload.audio_format)
    print("BITRATE:", payload.bitrate)
    print("==============================\n")

    try:

        download_playlist(
            playlist_url=payload.playlist_url,
            output_dir=temp_dir,
            audio_format=payload.audio_format,
            bitrate=payload.bitrate
        )

        print("Download finished")

        zip_path = shutil.make_archive(
            base_name=temp_dir,
            format="zip",
            root_dir=temp_dir
        )

        print("ZIP CREATED:", zip_path)

        background_tasks.add_task(
            shutil.rmtree,
            temp_dir,
            ignore_errors=True
        )

        background_tasks.add_task(
            os.remove,
            zip_path
        )

        return FileResponse(
            path=zip_path,
            media_type="application/zip",
            filename="spotify_playlist.zip",
            background=background_tasks
        )

    except Exception as e:

        print("\n========== ERROR ==========")
        traceback.print_exc()
        print("===========================\n")

        shutil.rmtree(
            temp_dir,
            ignore_errors=True
        )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )