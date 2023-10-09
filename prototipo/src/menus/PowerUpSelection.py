class PowerUpSelection:
    def __init__(self, avaliable_power_ups: list):
       self.__avaliable_power_ups = avaliable_power_ups

    @property
    def avaliable_power_ups(self):
        return self.__avaliable_power_ups

    @avaliable_power_ups.setter
    def avaliable_power_ups(self, val:list):
        if isinstance(val, list):
            self.__avaliable_power_ups = val