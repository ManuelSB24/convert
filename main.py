import tkinter as tk
from tkinter import filedialog, messagebox
import os
from audios import Audios

class AudioConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Converter")

        self.input_folder = ""
        self.output_folder = ""

        self.create_widgets()

    def create_widgets(self):
        self.input_label = tk.Label(self.root, text="Carpeta de entrada:")
        self.input_label.pack(pady=5)

        self.input_entry = tk.Entry(self.root, width=50)
        self.input_entry.pack(pady=5)

        self.input_button = tk.Button(self.root, text="Seleccionar carpeta", command=self.select_input_folder)
        self.input_button.pack(pady=5)

        self.output_label = tk.Label(self.root, text="Carpeta de salida:")
        self.output_label.pack(pady=5)

        self.output_entry = tk.Entry(self.root, width=50)
        self.output_entry.pack(pady=5)

        self.output_button = tk.Button(self.root, text="Seleccionar carpeta", command=self.select_output_folder)
        self.output_button.pack(pady=5)

        self.convert_button = tk.Button(self.root, text="Convertir", command=self.convert)
        self.convert_button.pack(pady=20)

    def select_input_folder(self):
        self.input_folder = filedialog.askdirectory()
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, self.input_folder)

    def select_output_folder(self):
        self.output_folder = filedialog.askdirectory()
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, self.output_folder)

    def convert(self):
        self.input_folder = self.input_entry.get()
        self.output_folder = self.output_entry.get()

        if not self.input_folder or not self.output_folder:
            messagebox.showerror("Error", "Debe seleccionar ambas carpetas")
            return

        if not os.listdir(self.input_folder):
            messagebox.showerror("Error", "La carpeta de entrada está vacía")
            return

        if not os.access(self.output_folder, os.W_OK):
            messagebox.showerror("Error", "No se puede escribir en la carpeta de salida")
            return

        try:
            Audios.batch_convert_mp4_to_mp3(self.input_folder, self.output_folder)
            messagebox.showinfo("Éxito", "Conversión completada")
        except Exception as e:
            messagebox.showerror("Error", f"Error al procesar los archivos: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioConverterApp(root)
    root.mainloop()
