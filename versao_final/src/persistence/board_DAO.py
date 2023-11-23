from persistence.DAO import DAO

class BoardDAO(DAO):
    def __init__(self):
        super().__init__('persistence/data/board.json')