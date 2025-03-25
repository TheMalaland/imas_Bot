import subprocess
import os
import sys

def download_youtube_live(url, download_path):
    # Crear la carpeta de descarga si no existe
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    try:
        # Comando para descargar el video en vivo con la máxima calidad en la carpeta especificada
        command = ['yt-dlp', '-f', 'best', '--restrict-filenames', '-o', os.path.join(download_path, '%(title)s.%(ext)s'), url]
        process = subprocess.Popen(command)

        print("Descargando... Presiona Ctrl+C para detener.")
        # Espera a que el proceso termine o sea interrumpido
        process.wait()
    except subprocess.CalledProcessError as e:
        print(f"Error al descargar el video: {e}")
    except KeyboardInterrupt:
        print("Descarga interrumpida por el usuario.")
        process.terminate()
        process.wait()
    finally:
        if process.poll() is None:
            process.terminate()
            process.wait()

if __name__ == "__main__":
    url = input("Introduce la URL del video en vivo de YouTube: ")
    download_path = "descargas_youtube_live"  # Cambia esto si deseas otra carpeta
    download_youtube_live(url, download_path)