from game_types.game_standard import Game

from collections import Counter
import json
import pandas
from tqdm import tqdm


def load_config():
    return json.load(open('python3/config.json', 'r'))


def main():
    stats = []
    config = load_config()
    
    for _ in tqdm(range(int(1000)), ascii=True, desc='Playing war games'):
        stats.append(Game(config).play())
    
    df = pandas.DataFrame(list(map(lambda x: dict(x), stats))).fillna(0)
    for col in df.columns:
        if col.endswith('won'):
            print('{}: {}'.format(col, df[col].sum()))
        else:
            print('{}: {}'.format(col, df[col].mean()))


if __name__ == '__main__':
    main()