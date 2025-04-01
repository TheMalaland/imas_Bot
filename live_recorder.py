"""
This code downloads a live stream from YouTube and saves it two files in the best quality available.
the files will be saved in the directory youtube_live_recordings_5min_madoka2 or the one you
specify in the OUTPUT_FOLDER variable. 

When the user needs to stops the recording, the program will stop and save the last segment recorded.
use the command "Ctrl + C" to stop the recording. it will take some time to unify all files

order
                                                      (If desired)     (if desired)  
live_recorder.py ==> convertmp4.py ==> combine.py ==> divideby.py ==> 4kconverter.py

"""""
import os
import time
import subprocess
from datetime import datetime

# URL del live de YouTube
YOUTUBE_LIVE_URL = "https://www.youtube.com/watch?v=4NBT677Thkg"

# Duración de cada fragmento en segundos (5 minutos = 300s)
BLOCK_DURATION = 300  

# Carpeta donde se guardarán los videos
OUTPUT_FOLDER = "youtube_live_recordings_5min_madoka"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def check_video_availability(url):
    command = ["yt-dlp", "--skip-download", url]
    process = subprocess.run(command, capture_output=True, text=True)
    if "Video unavailable" in process.stderr:
        return False
    return True

def record_live():
    if not check_video_availability(YOUTUBE_LIVE_URL):
        print("⛔ El video no está disponible. Verifique la URL o si el live está activo.")
        return

    block_number = 1

    while True:
        # Crear nombre del archivo con timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_filename = os.path.join(OUTPUT_FOLDER, f"live_part_{block_number}_{timestamp}.mp4")

        print(f"📡 Grabando bloque {block_number} en máxima calidad...")

        # Comando para grabar el stream en la mejor calidad
        command = [
            "yt-dlp",
            "-f", "bestvideo+bestaudio/best",  # Máxima calidad de video y audio
            "--merge-output-format", "mp4",  # Fuerza salida en MP4
            "--hls-use-mpegts",  # Previene errores de segmentación
            "--live-from-start",  # Intenta descargar desde el inicio si es posible
            "-o", output_filename,
            "--external-downloader", "ffmpeg",
            "--external-downloader-args", f"-t {BLOCK_DURATION}",
            YOUTUBE_LIVE_URL
        ]

        try:
            # Ejecutar la grabación
            process = subprocess.run(command, capture_output=True, text=True)
            
            # Si el proceso termina con error, probablemente el live haya acabado
            if process.returncode != 0:
                print(f"⛔ Live finalizado o error en la conexión. Código de retorno: {process.returncode}")
                print(f"Error: {process.stderr}")
                break

        except Exception as e:
            print(f"⚠️ Error al ejecutar el comando: {e}")
            break

        block_number += 1
        time.sleep(5)  # Pequeño delay entre grabaciones

if __name__ == "__main__":
    record_live()