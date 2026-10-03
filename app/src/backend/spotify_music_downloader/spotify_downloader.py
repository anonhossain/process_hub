# #app/src/backend/spotify_music_downloader/spotify_downloader.py

# import os
# import subprocess


# def download_playlist(
#     playlist_url,
#     output_dir,
#     audio_format="m4a",
#     bitrate="256k",
#     ffmpeg_path=r"C:\files\ffmpeg\bin\ffmpeg.exe"
# ):
#     # Create output directory
#     os.makedirs(output_dir, exist_ok=True)

#     print("Spotify Playlist:")
#     print(playlist_url)

#     print("\nOutput folder:")
#     print(output_dir)

#     print("\nFormat:")
#     print(audio_format.upper())

#     print("\nBitrate:")
#     print(bitrate)

#     print("\nStarting download...\n")

#     command = [
#         "spotdl",
#         "download",
#         playlist_url,
#         "--output",
#         f"{output_dir}/{{title}}.{{output-ext}}",
#         "--format",
#         audio_format,
#         "--bitrate",
#         bitrate,
#         "--ffmpeg",
#         ffmpeg_path
#     ]

#     try:
#         subprocess.run(command, check=True)

#         print("\nDownload completed!")
#         print(f"Files saved to: {output_dir}")

#     except subprocess.CalledProcessError as e:
#         print("\nDownload failed!")
#         print(f"Error code: {e.returncode}")


# if __name__ == "__main__":

#     playlist_url = "https://open.spotify.com/playlist/2Saza0damn2pxkLF32JJIp?si=0ff9d02f2fef4c9f"
#     output_dir ="app\\output"
#     audio_format = "m4a"
#     bitrate = "256k"

#     download_playlist(
#         playlist_url,
#         output_dir,
#         audio_format,
#         bitrate
#     )

# import os
# import subprocess


# def download_playlist(
#     playlist_url,
#     output_dir,
#     audio_format="m4a",
#     bitrate="256k",
#     ffmpeg_path=r"C:\files\ffmpeg\bin\ffmpeg.exe"
# ):

#     # Create output directory
#     os.makedirs(output_dir, exist_ok=True)

#     # spotDL executable inside your current virtual environment
#     spotdl_path = r"C:\files\process_hub\.venv\Scripts\spotdl.exe"

#     print("Spotify Playlist:")
#     print(playlist_url)

#     print("\nOutput folder:")
#     print(output_dir)

#     print("\nFormat:")
#     print(audio_format.upper())

#     print("\nBitrate:")
#     print(bitrate)

#     print("\nStarting download...\n")

#     command = [
#         spotdl_path,
#         "download",
#         playlist_url,
#         "--output",
#         f"{output_dir}/{{title}}.{{output-ext}}",
#         "--format",
#         audio_format,
#         "--bitrate",
#         bitrate,
#         "--ffmpeg",
#         ffmpeg_path
#     ]

#     try:
#         subprocess.run(command, check=True)

#         print("\nDownload completed!")
#         print(f"Files saved to: {output_dir}")

#     except subprocess.CalledProcessError as e:
#         print("\nDownload failed!")
#         print(f"Error code: {e.returncode}")

#     except FileNotFoundError as e:
#         print("\nRequired executable not found!")
#         print(e)


# if __name__ == "__main__":

#     playlist_url = "https://open.spotify.com/playlist/2Saza0damn2pxkLF32JJIp?si=0ff9d02f2fef4c9f"

#     output_dir = r"app\output"

#     audio_format = "m4a"

#     bitrate = "256k"

#     download_playlist(
#         playlist_url,
#         output_dir,
#         audio_format,
#         bitrate
#     )

#============================= API VERSION =============================

import os
import subprocess

def download_playlist(
    playlist_url,
    output_dir,
    audio_format="m4a",
    bitrate="256k",
    ffmpeg_path=r"C:\files\ffmpeg\bin\ffmpeg.exe"
):

    os.makedirs(output_dir, exist_ok=True)

    command = [
        "spotdl",
        "download",
        playlist_url,
        "--output",
        f"{output_dir}/{{title}}.{{output-ext}}",
        "--format",
        audio_format,
        "--bitrate",
        bitrate,
        "--ffmpeg",
        ffmpeg_path
    ]

    subprocess.run(command, check=True)


import os
import sys
import subprocess


def download_playlist(
    playlist_url,
    output_dir,
    audio_format="m4a",
    bitrate="256k",
    ffmpeg_path=r"C:\files\ffmpeg\bin\ffmpeg.exe"
):

    os.makedirs(output_dir, exist_ok=True)

    print("Spotify Playlist:", playlist_url)
    print("Output folder:", output_dir)
    print("Format:", audio_format)
    print("Bitrate:", bitrate)

    command = [
        sys.executable,
        "-m",
        "spotdl",
        "download",
        playlist_url,

        "--output",
        os.path.join(
            output_dir,
            "{title}.{output-ext}"
        ),

        "--format",
        audio_format,

        "--bitrate",
        bitrate,

        "--ffmpeg",
        ffmpeg_path
    ]

    print("\nRunning command:")
    print(command)

    subprocess.run(
        command,
        check=True
    )

    print("\nDownload completed!")