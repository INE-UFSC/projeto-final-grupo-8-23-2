class Menu:
    def __init__(self, buttons: list, background: str):
       self.__buttons = buttons
       self.__background = background

    @property
    def buttons(self):
        return self.__buttons

    @buttons.setter
    def buttons(self, val:list):
        if isinstance(val, list):
            self.__buttons = val

    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, val:str):
        if isinstance(val, str):
            self.__background = val
