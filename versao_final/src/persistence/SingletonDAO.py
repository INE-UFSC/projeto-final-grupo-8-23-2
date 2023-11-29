# create a singleton pattern for boardDAO

from persistence.board_DAO import BoardDAO

class SingletonDAO(BoardDAO):
    __instance = None
    def __init__(self):
        if SingletonDAO.__instance == None:
            super().__init__()
            SingletonDAO.__instance = self
        else:
            raise Exception("You cannot create another SingletonDAO class")
    
    @staticmethod
    def get_instance():
        if SingletonDAO.__instance == None:
            SingletonDAO()
        return SingletonDAO.__instance
