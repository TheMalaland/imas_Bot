import subprocess

# Rutas de los archivos de entrada y salida
input_file = "youtube_live_recordings_5min_madoka\segments\Idolmaster Shiny Colors Song For Prism 24_7 live #part1.mp4"
output_file = "youtube_live_recordings_5min_madoka\segments\Idolmaster Shiny Colors Song For Prism 24_7 live #part1_4k.mp4"
# Comando para convertir el video de Full HD a 4K
command = [
    "ffmpeg",
    "-i", input_file,
    "-vf", "scale=3840:2160",
    "-c:a", "copy",
    output_file
]

# Ejecutar el comando
subprocess.run(command, check=True)

print(f"✅ Video convertido a 4K: {output_file}")