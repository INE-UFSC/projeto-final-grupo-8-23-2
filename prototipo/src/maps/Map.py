class Map:
    def __init__(self, height: int, width: int, background: str):
       self.__height = height
       self.__width = width
       self.__background = background
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val:int):
        if isinstance(val, int):
            self.__height = val

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val:int):
        if isinstance(val, int):
            self.__width = val

    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, val:str):
        if isinstance(val, str):
            self.__background = val
            
    def load_map():
        pass
    
    def update_map():
        pass