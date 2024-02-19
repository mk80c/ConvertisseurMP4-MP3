import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from moviepy.editor import *

def convert_mp4_to_mp3(mp4_files):
    for mp4_file in mp4_files:
        mp3_file = os.path.splitext(mp4_file)[0] + ".mp3"
        video_clip = AudioFileClip(mp4_file)
        video_clip.write_audiofile(mp3_file)

    messagebox.showinfo("Conversion réussie", "La conversion a été effectuée avec succès !")

def choose_files():
    mp4_files = filedialog.askopenfilenames(filetypes=[("MP4 files", "*.mp4")])
    if mp4_files:
        try:
            convert_mp4_to_mp3(mp4_files)
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")
    else:
        messagebox.showerror("Erreur", "Aucun fichier sélectionné.")

# Créer une fenêtre
window = tk.Tk()
window.title("Convertisseur MP4 vers MP3")

# Bouton pour choisir les fichiers MP4
choose_button = tk.Button(window, text="Choisir des fichiers MP4", command=choose_files)
choose_button.pack(pady=20)

# Exécuter la boucle principale
window.mainloop()
