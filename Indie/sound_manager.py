from Indie.gameobject import GAMEOBJECT
from pygame import mixer

# Starting the mixer
mixer.init()


class MUSIC(GAMEOBJECT):
    """
    Manages the background music
    """
    path = ""
    
    def __init__(self,path:str) -> None:
        self.path = path
        mixer.music.load(path)

    def play(self,loops:int = -1,start:float=0.0,fade_ms:int=10):
        """
        Play music (background music)
        Parameters:
        :loops(int): how many times to loop the the music, -1 for infite loops
        :start(float): from which position of the time to start playing
        :fade_ms(int): the duration required to fade in
        """
        mixer.music.play(loops=loops,start=start,fade_ms=fade_ms)

    def volume(self,volume:float):
        """
        Set the volume of the music
        Parameters:
        volume(float): range from 0 to 1
        """
        mixer.music.set_volume(volume)

    def pause(self):
        mixer.music.pause()
    
    def unpause(self):
        mixer.music.unpause()
    
    def stop(self):
        mixer.music.stop()
        mixer.music.unload
        
    def fadeout(self):
        mixer.music.fadeout()

class SOUND():
    sounds = {}
    def add(self,name:str,path:str):
        """
        Add sound int the sounds library
        
        Parameters:
        :name(str): the name of the sound for playing 
        :path(str): the path of the sound to be added
        """
        self.sounds[name] = mixer.Sound(path)

    def remove(self,name:str):
        """
        Remove sounds after use

        Parameters:
        :name(str): the name of sound to remove
        """
        del self.sounds[name]

    def play(self,name:str):
        """
        Play a sound

        Parameters:
        :name(str): name of the sound to be played
        """
        mixer.Sound.play(self.sounds[name])
        