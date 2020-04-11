import argparse
from collections import Counter
import json
import pandas
from tqdm import tqdm
from config import Config


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nbattles')

    global _args
    _args = parser.parse_args()


def main():
    stats = []
    config = Config().get_config()

    if _args.nbattles:
        config.games.number_of_games = _args.nbattles
    
    for _ in tqdm(range(int(config.games.number_of_games)), ascii=True, desc='Playing war games'):
        g = config.games.game_type(config)
        stats.append(g.play())
    
    df = pandas.DataFrame(list(map(lambda x: dict(x), stats))).fillna(0)
    for col in df.columns:
        if col.endswith('won'):
            print('{}: {}'.format(col, df[col].sum()))
        else:
            print('{}: {}'.format(col, df[col].mean()))


if __name__ == '__main__':
    parse_args()
    main()