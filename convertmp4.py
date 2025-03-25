"""
this script is used to convert the .part files to .mp4 files
"""

import os
import subprocess

# Carpeta donde se encuentran los archivos .part
INPUT_FOLDER = "youtube_live_recordings_5min_madoka"

def convert_part_to_mp4(input_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".part"):
            input_filepath = os.path.join(input_folder, filename)
            output_filepath = os.path.splitext(input_filepath)[0] + ".mp4"
            
            # Comando para convertir el archivo .part a .mp4 usando ffmpeg
            command = [
                "ffmpeg",
                "-i", input_filepath,
                "-c:v", "copy",
                "-c:a", "copy",
                output_filepath
            ]
            
            try:
                # Ejecutar la conversión
                subprocess.run(command, check=True)
                print(f"✅ Archivo convertido: {output_filepath}")
            except subprocess.CalledProcessError as e:
                print(f"⚠️ Error al convertir el archivo {input_filepath}: {e}")

if __name__ == "__main__":
    convert_part_to_mp4(INPUT_FOLDER)