from persistence.DAO import DAO

class BoardDAO(DAO):
    def __init__(self):
        super().__init__('persistence/data/board.json')
        self.__name = ''

    def get_players_name(self)-> list[str]:
        return [elements['name'] for elements in self.cache]
        
    def get_players_score(self)-> list[str]:
        return [elements['score'] for elements in self.cache]
    
    def get_players_time(self)-> list[str]:
        return [elements['time'] for elements in self.cache]

    def get_players(self)-> list[dict]:
        return self.cache
    
    def search_player(self, name: str)-> dict:
        for elements in self.cache:
            if elements['name'] == name:
                return elements
        return None
    
    def add_player(self, score: int, time: int):
        if self.__name not in self.get_players_name():
            self.cache.append({'name': self.__name, 'score': score, 'time': time})
        else:
            if self.search_player(self.__name)['score'] < score:
                self.search_player(self.__name)['score'] = score
                self.search_player(self.__name)['time'] = time
        self.sort_players()

    def sort_players(self):
        self.cache = sorted(self.cache, key=lambda x: x['score'], reverse=True)        

    def delete_player(self, name: str):
        self.cache.remove(self.search_player(name))

    def set_name(self, name: str):
        self.__name = name
