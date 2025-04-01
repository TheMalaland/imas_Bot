import os
import subprocess

def download_youtube_video():
    # Solicitar la URL del video
    url = input("Ingresa la URL del video de YouTube: ")

    # Crear la carpeta "downloads" si no existe
    download_folder = "downloads"
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Comando para descargar el video con yt-dlp
    command = [
        "yt-dlp",
        "-f", "bestvideo+bestaudio/best",  # Seleccionar la mejor calidad de video y audio
        "--merge-output-format", "mp4",   # Combinar video y audio en formato MP4
        "--output", f"{download_folder}/%(title)s.%(ext)s",  # Ruta de salida
        "--progress",                     # Mostrar progreso
    ]

    # Agregar la URL al comando
    command.append(url)

    try:
        # Ejecutar el comando
        subprocess.run(command, check=True)
        print(f"Descarga completada. Archivo guardado en: {os.path.abspath(download_folder)}")
    except subprocess.CalledProcessError as e:
        print(f"Error al descargar el video: {e}")

if __name__ == "__main__":
    download_youtube_video()