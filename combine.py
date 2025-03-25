"""
this script is used to combine the audio and video files into a single file


"""

import os
import subprocess

# Rutas de los archivos de audio y video
AUDIO_FILE = "youtube_live_recordings_5min_madoka\\audio.mp4"  # Asegúrate de que esta ruta sea correcta
VIDEO_FILE = "youtube_live_recordings_5min_madoka\\video.mp4"
OUTPUT_FILE = "youtube_live_recordings_5min_madoka\\merged_output.mp4"

def merge_audio_video(audio_file, video_file, output_file):
    if os.path.exists(audio_file) and os.path.exists(video_file):
        # Comando para combinar el archivo de audio y video usando ffmpeg
        command = [
            "ffmpeg",
            "-i", video_file,
            "-i", audio_file,
            "-c:v", "copy",
            "-c:a", "copy",
            output_file
        ]
        
        try:
            # Ejecutar la combinación
            subprocess.run(command, check=True)
            print(f"✅ Archivos combinados: {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Error al combinar los archivos {audio_file} y {video_file}: {e}")
    else:
        if not os.path.exists(audio_file):
            print(f"⚠️ No se encontró el archivo de audio: {audio_file}")
        if not os.path.exists(video_file):
            print(f"⚠️ No se encontró el archivo de video: {video_file}")

if __name__ == "__main__":
    merge_audio_video(AUDIO_FILE, VIDEO_FILE, OUTPUT_FILE)