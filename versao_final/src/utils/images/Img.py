

import pygame

class Img():
    def __init__(self, name, path, height=0, width=0, flip_x=False, flip_y=False) -> None:
        self.__name = name
        self.__path = path
        self.__height = height
        self.__width = width
        self.__flip_x = flip_x
        self.__flip_y = flip_y
    
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
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, val):
        self.__height = val
        
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, val):
        self.__width = val
        
    @property
    def flip_x(self):
        return self.__flip_x

    @flip_x.setter
    def flip_x(self, val:bool):
        if isinstance(val, bool):
            self.__flip_x = val

    @property
    def flip_y(self):
        return self.__flip_y

    @flip_y.setter
    def flip_y(self, val:bool):
        if isinstance(val, bool):
            self.__flip_y = val
        
    def transform_scale(self):
        return pygame.transform.scale(pygame.image.load(self.path),
                                              (self.width, self.height))
        
    def transform_flip(self, flip_x=False, flip_y=False):
        return pygame.transform.flip(self.transform_scale(), flip_x, flip_y)
    
    def transform_rotate(self, deg:int):
        return pygame.transform.rotate(self.transform_scale(), deg)
    
    def transform_scale_2x(self):
        return pygame.transform.scale2x(pygame.image.load(self.path))
    