import pygame

class Sound():
    def __init__(self, name, path, volumn = 1, is_bg=True) -> None:
        self.__name = name
        self.__path = path
        self.__volumn = volumn
        self.__is_bg = is_bg
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, val):
        self.__name = val
    
    @property
    def path(self):
        return self.__path
    
    @path.setter
    def path(self, val):
        self.__path = val
        
    @property
    def volumn(self):
        return self.__volumn
    
    @volumn.setter
    def volumn(self, val):
        self.__volumn = val
        
    @property
    def is_bg(self):
        return self.__is_bg
    
    @is_bg.setter
    def is_bg(self, val):
        self.__is_bg = val
        
    def run(self):
        if self.__is_bg:
            self.run_bg()
        else:
            self.run_temp()
        
    def run_bg(self) -> None:
        pygame.mixer.init()
        pygame.mixer.music.set_volume(self.__volumn)
        pygame.mixer.music.load(self.__path)
        pygame.mixer.music.play(-1)
        
    # run sem pausar a musica de fundo
    def run_temp(self) -> None:
        sound = pygame.mixer.Sound(self.__path)
        sound.set_volume(self.__volumn)
        sound.play()