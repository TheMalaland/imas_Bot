import os
import subprocess

# Ruta del archivo de video
VIDEO_FILE = "youtube_live_recordings_5min_madoka\\merged_output.mp4"
OUTPUT_DIR = "youtube_live_recordings_5min_madoka\\segments"
SEGMENTS = 10

# Crear el directorio de salida si no existe
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Obtener la duración total del video
result = subprocess.run(
    ["ffmpeg", "-i", VIDEO_FILE],
    stderr=subprocess.PIPE,
    universal_newlines=True
)
duration_line = [x for x in result.stderr.split('\n') if "Duration" in x][0]
duration = duration_line.split(",")[0].split("Duration:")[1].strip()
h, m, s = map(float, duration.split(":"))
total_seconds = int(h * 3600 + m * 60 + s)

# Calcular la duración de cada segmento
segment_duration = total_seconds // SEGMENTS

# Dividir el video en segmentos
for i in range(SEGMENTS):
    start_time = i * segment_duration
    output_file = os.path.join(OUTPUT_DIR, f"segment_{i+1}.mp4")
    command = [
        "ffmpeg",
        "-i", VIDEO_FILE,
        "-ss", str(start_time),
        "-t", str(segment_duration),
        "-c", "copy",
        output_file
    ]
    subprocess.run(command)

print(f"✅ Video dividido en {SEGMENTS} partes iguales en el directorio {OUTPUT_DIR}")