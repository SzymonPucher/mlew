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

    def get_config(self):
        return type('Expando', (object,), Config.dfs(self.config_json))
