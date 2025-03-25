import os

# Ruta del directorio de segmentos
SEGMENTS_DIR = "youtube_live_recordings_5min_madoka\\segments"
NEW_NAME_TEMPLATE = "Idolmaster Shiny Colors Song For Prism 24_7 live #part{}.mp4"

# Obtener la lista de archivos en el directorio de segmentos
files = sorted(os.listdir(SEGMENTS_DIR))

# Renombrar cada archivo
for i, filename in enumerate(files):
    old_file_path = os.path.join(SEGMENTS_DIR, filename)
    new_file_name = NEW_NAME_TEMPLATE.format(i + 1)
    new_file_path = os.path.join(SEGMENTS_DIR, new_file_name)
    
    os.rename(old_file_path, new_file_path)
    print(f"Renombrado: {old_file_path} -> {new_file_path}")

print(f"✅ Todos los archivos en {SEGMENTS_DIR} han sido renombrados.")