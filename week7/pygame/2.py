from tkinter import *
from tkinter import filedialog
from pygame import mixer
import pygame
class MusicPlayer:
    def __init__(self, window ):
        pygame.init()
        window.geometry('320x100'); window.title('Iris Player'); window.resizable(0,0)
        Previous = Button(window, text = 'Previous',  width = 10, font = ('Times', 10), command = self.previous)
        Play = Button(window, text = 'Play/Stop',  width = 10,font = ('Times', 10), command = self.play)
        Pause = Button(window,text = 'Pause',  width = 10, font = ('Times', 10), command = self.pause)
        Next = Button(window ,text = 'Next',  width = 10, font = ('Times', 10), command = self.next)
        Previous.place(x=0,y=20);Play.place(x=110,y=20);Pause.place(x=110,y=60);Next.place(x=220,y=20) 
        self.music_file = pygame.mixer.music.load('c:/Users/User/Desktop/pp2_homework/PP2_Homework-8/week7/pygame/song1.mp3')
        self.playing_state = False
        self.play_state= False
        self.k=0

    def previous(self):
        if self.k==0:
            pygame.mixer.music.load('c:/Users/User/Desktop/pp2_homework/PP2_Homework-8/week7/pygame/song3.mp3')
            pygame.mixer.music.play()
            self.k=2
        elif self.k==1:
            pygame.mixer.music.load('c:/Users/User/Desktop/pp2_homework/PP2_Homework-8/week7/pygame/song1.mp3')
            pygame.mixer.music.play()
            self.k=0
        elif self.k==2:
            pygame.mixer.music.load('c:/Users/User/Desktop/pp2_homework/PP2_Homework-8/week7/pygame/song2.mp3')
            pygame.mixer.music.play()
            self.k=1
    def play(self):
        if not self.play_state:
            mixer.music.play()
            self.play_state= True
        else:
            mixer.music.stop()
            self.play_state= False
    def pause(self):
        if not self.play_state:
            pass
        else:
            if not self.playing_state:
                mixer.music.pause()
                self.playing_state=True
            else:
                mixer.music.unpause()
                self.playing_state = False
    def next(self):
         if self.k==0:
            pygame.mixer.music.load('c:/Users/User/Desktop/pp2_homework/PP2_Homework-8/week7/pygame/song2.mp3')
            pygame.mixer.music.play()
            self.k=1
         elif self.k==1:
            pygame.mixer.music.load('c:/Users/User/Desktop/pp2_homework/PP2_Homework-8/week7/pygame/song3.mp3')
            pygame.mixer.music.play()
            self.k=2
         elif self.k==2:
            pygame.mixer.music.load('c:/Users/User/Desktop/pp2_homework/PP2_Homework-8/week7/pygame/song1.mp3')
            pygame.mixer.music.play()
            self.k=0
root = Tk()
app= MusicPlayer(root)
root.mainloop()