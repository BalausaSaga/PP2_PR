import pygame
import os

class MusicPlayer:
    def __init__(self, music_dir):
        self.playlist = [os.path.join(music_dir, f) for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav'))]
        self.current_track = 0
        
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_track])

    def play(self):
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next(self):
        self.current_track = (self.current_track + 1) % len(self.playlist)
        pygame.mixer.music.load(self.playlist[self.current_track])
        self.play()

    def prev(self):
        self.current_track = (self.current_track - 1) % len(self.playlist)
        pygame.mixer.music.load(self.playlist[self.current_track])
        self.play()