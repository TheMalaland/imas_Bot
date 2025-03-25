import os
import time
import subprocess
from datetime import datetime

# URL del live de YouTube
YOUTUBE_LIVE_URL = "https://www.youtube.com/watch?v=DYEKgTskSzc"

# Duración de cada fragmento en segundos (1 hora = 3600s)
BLOCK_DURATION = 3600  

# Carpeta donde se guardarán los videos
OUTPUT_FOLDER = "youtube_live_recordings_5"
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

        # Ejecutar la grabación
        process = subprocess.run(command)

        # Si el proceso termina con error, probablemente el live haya acabado
        if process.returncode != 0:
            print("⛔ Live finalizado o error en la conexión. Deteniendo grabación.")
            break

        block_number += 1
        time.sleep(5)  # Pequeño delay entre grabaciones

if __name__ == "__main__":
    record_live()