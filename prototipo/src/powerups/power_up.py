class PowerUp:
    def __init__(self, quantity: float, icon: str, type: str):
       self.__quantity = quantity
       self.__icon = icon
       self.__type = type

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, val:float):
        if isinstance(val, float):
            self.__quantity = val

    @property
    def icon(self):
        return self.__icon

    @icon.setter
    def icon(self, val:str):
        if isinstance(val, str):
            self.__icon = val

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, val:str):
        if isinstance(val, str):
            self.__type = val

    def power_up_logic(self) -> None:
        pass
    
    def activate_power_up(self) -> None:
        pass