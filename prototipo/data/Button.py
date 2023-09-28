class Button:
    def __init__(self, height: int, width: int, coordinate_x: int, coordinate_y: int, icon: str):
       self.__height = height
       self.__width = width
       self.__coordinate_x = coordinate_x
       self.__coordinate_y = coordinate_y
       self.__icon = icon
       
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
    def coordinate_x(self):
        return self.__coordinate_x

    @coordinate_x.setter
    def coordinate_x(self, val:int):
        if isinstance(val, int):
            self.__coordinate_x = val

    @property
    def coordinate_y(self):
        return self.__coordinate_y

    @coordinate_y.setter
    def coordinate_y(self, val:int):
        if isinstance(val, int):
            self.__coordinate_y = val

    @property
    def icon(self):
        return self.__icon

    @icon.setter
    def icon(self, val:str):
        if isinstance(val, str):
            self.__icon = val
            
    def click_button():
        pass
