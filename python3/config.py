import json
import os

class Config:

    def __init__(self):
        self.config_json = Config.load_config_json(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json'))
    
    @staticmethod
    def load_config_json(path):
        try:
            return json.load(open(path, 'r'))
        except FileNotFoundError as e:
            print(e)
            raise
        except Exception as e:
            print(e)
            raise

    @staticmethod
    def dfs(d):
        for i in d.keys():
            if isinstance(d[i], list):
                for j in range(len(d[i])):
                    Config.dfs(d[i][j])
                    d[i][j] = type('Expando', (object,), d[i][j])
            if isinstance(d[i], dict):
                Config.dfs(d[i])
                d[i] = type('Expando', (object,), d[i])
        return d

    @staticmethod
    def convert_card_type(type_str):
        if type_str == 'base':
            from card_types.card_base import CardBase
            return CardBase
        elif type_str == 'unique':
            from card_types.card_unique import CardUnique
            return CardUnique
        else:
            raise NameError('Incorrect type of the card: {}'.format(type_str))

    @staticmethod
    def convert_player_type(type_str):
        if type_str == 'base':
            from player_types.player_base import PlayerBase
            return PlayerBase
        elif type_str == 'shuffleless':
            from player_types.player_shuffleless import PlayerShuffleless
            return PlayerShuffleless
        elif type_str == 'inreverse':
            from player_types.player_inreverse import PlayerInreverse
            return PlayerInreverse
        else:
            raise NameError('Incorrect type of the player: {}'.format(type_str))
    
    @staticmethod
    def convert_game_type(type_str):
        if type_str == 'base':
            from game_types.game_base import GameBase
            return GameBase
        else:
            raise NameError('Incorrect type of the game: {}'.format(type_str))
    
    @staticmethod
    def convert_operation(operation_str):
        if operation_str == 'sum':
            return lambda df: df.sum()
        if operation_str == 'avg':
            return lambda df: df.mean()
        raise NameError('Incorrect type of the operation: {}'.format(operation_str))

    
    def get_config(self):
        obj = type('Expando', (object,), Config.dfs(self.config_json))
        obj.games.game_type = Config.convert_game_type(obj.games.game_type)
        obj.games.card_type = Config.convert_card_type(obj.games.card_type)
        
        for i in range(len(obj.players)):
            obj.players[i].type = Config.convert_player_type(obj.players[i].type)

        for i in range(len(obj.analysis.columns)):
            obj.analysis.columns[i].operation = Config.convert_operation(obj.analysis.columns[i].operation)

        return obj
