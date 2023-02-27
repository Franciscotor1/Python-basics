import moviepy.editor as mp
import pygame
import os
import sys
import tkinter as tk
from tkinter import filedialog

# Inicializar tkinter
root = tk.Tk()
root.withdraw() # Oculta la ventana principal de tkinter

# Pide al usuario que seleccione los archivos de video
file_paths = filedialog.askopenfilenames(title="Selecciona los archivos de video", filetypes=[("Archivos de video", "*.mp4 *.avi *.mov")])

pygame.init()

# Define el tamaño de la ventana
SCREEN_SIZE = (640, 480)

# Crea la ventana
screen = pygame.display.set_mode(SCREEN_SIZE)

# Crea la lista de reproducción
playlist = []

# Agrega los archivos de video seleccionados a la lista de reproducción
for file_path in file_paths:
    clip = mp.VideoFileClip(file_path)
    playlist.append(clip)

# Convierte el video en un objeto Pygame
current_video = playlist[0].resize(SCREEN_SIZE).set_pos((0,0)).to_ImageClip().to_videotexture()

try:
    # Reproduce el video
    current_video.play()

    # Mientras se está reproduciendo el video, actualiza la ventana
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_video.stop()
                pygame.quit()
                sys.exit()

        screen.blit(current_video.get_surface(), (0, 0))
        pygame.display.update()

        # Si el video actual termina, cambia al siguiente video en la lista de reproducción
        if not current_video.get_busy():
            current_video.stop()
            playlist.pop(0)
            if len(playlist) > 0:
                current_video = playlist[0].resize(SCREEN_SIZE).set_pos((0,0)).to_ImageClip().to_videotexture()
                current_video.play()
            else:
                pygame.quit()
                sys.exit()

except Exception as e:
    print("Ha ocurrido un error:", e)
    current_video.stop()
    pygame.quit()
    sys.exit()

