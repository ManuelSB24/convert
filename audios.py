from moviepy.editor import VideoFileClip
import os

class Audios():
    
    def convert_mp4_to_mp3(input_file, output_file):
        try:
            # Carga el archivo de video MP4
            video = VideoFileClip(input_file)
            # Extrae el audio y lo guarda como MP3
            video.audio.write_audiofile(output_file, codec='mp3')
            print(f"Archivo convertido y guardado como: {output_file}")
        except Exception as e:
            print(f"Error al convertir {input_file}: {e}")

    def batch_convert_mp4_to_mp3(input_folder, output_folder):
        # Verifica la existencia de la carpeta de entrada
        if not os.path.exists(input_folder):
            print(f"Error: la carpeta de entrada '{input_folder}' no existe.")
            return
        
        # Verifica si la carpeta de entrada está vacía
        if not os.listdir(input_folder):
            print(f"Advertencia: la carpeta de entrada '{input_folder}' está vacía.")
            return
        
        # Asegúrate de que la carpeta de salida exista
        os.makedirs(output_folder, exist_ok=True)
        
        # Itera sobre todos los archivos en la carpeta de entrada
        for filename in os.listdir(input_folder):
            if filename.endswith(".mp4"):
                input_file = os.path.join(input_folder, filename)
                output_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.mp3")
                Audios.convert_mp4_to_mp3(input_file, output_file)


