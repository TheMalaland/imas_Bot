import os
import subprocess
from datetime import datetime

# URL del live de YouTube
YOUTUBE_LIVE_URL = "https://www.youtube.com/watch?v=DYEKgTskSzc"

# Carpeta donde se guardarán los archivos
OUTPUT_FOLDER = "youtube_live_recordings_current"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def download_audio_video(url):
    # Crear nombre del archivo con timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    audio_filename = os.path.join(OUTPUT_FOLDER, f"live_audio_{timestamp}.mp3")
    video_filename = os.path.join(OUTPUT_FOLDER, f"live_video_{timestamp}.mp4")

    # Comando para descargar el audio en formato MP3
    audio_command = [
        "yt-dlp",
        "-f", "bestaudio",  # Máxima calidad de audio
        "--extract-audio",
        "--audio-format", "mp3",
        "-o", audio_filename,
        YOUTUBE_LIVE_URL
    ]

    # Comando para descargar el video en formato MP4
    video_command = [
        "yt-dlp",
        "-f", "bestvideo",  # Máxima calidad de video
        "-o", video_filename,
        YOUTUBE_LIVE_URL
    ]

    try:
        # Ejecutar la descarga de audio
        print(f"Ejecutando comando de audio: {' '.join(audio_command)}")
        audio_process = subprocess.run(audio_command, capture_output=True, text=True)
        print(f"Salida del comando de audio: {audio_process.stdout}")
        print(f"Errores del comando de audio: {audio_process.stderr}")

        # Ejecutar la descarga de video
        print(f"Ejecutando comando de video: {' '.join(video_command)}")
        video_process = subprocess.run(video_command, capture_output=True, text=True)
        print(f"Salida del comando de video: {video_process.stdout}")
        print(f"Errores del comando de video: {video_process.stderr}")

        # Verificar si las descargas fueron exitosas
        if audio_process.returncode == 0:
            print(f"✅ Audio descargado: {audio_filename}")
        else:
            print(f"⚠️ Error al descargar el audio: {audio_process.stderr}")

        if video_process.returncode == 0:
            print(f"✅ Video descargado: {video_filename}")
        else:
            print(f"⚠️ Error al descargar el video: {video_process.stderr}")

    except Exception as e:
        print(f"⚠️ Error al ejecutar el comando: {e}")

if __name__ == "__main__":
    download_audio_video(YOUTUBE_LIVE_URL)