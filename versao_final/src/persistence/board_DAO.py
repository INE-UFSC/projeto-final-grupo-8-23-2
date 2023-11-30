from persistence.DAO import DAO

class BoardDAO(DAO):
    def __init__(self):
        super().__init__('persistence/data/board.json')

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
    
    def add_player(self, name: str, score: int, time: int):
        if name not in self.get_players_name():
            self.cache.append({'name': name, 'score': score, 'time': time})
        else:
            if self.search_player(name)['score'] < score:
                self.search_player(name)['score'] = score
                self.search_player(name)['time'] = time
        self.sort_players()

    def sort_players(self):
        self.cache.sort(key=lambda x: x['score'], reverse=False)
        self.cache.sort(key=lambda x: x['time'])

    def delete_player(self, name: str):
        self.cache.remove(self.search_player(name))
