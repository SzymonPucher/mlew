import argparse
from collections import Counter, OrderedDict
from config import Config
import json
import pandas
from tqdm import tqdm



def parse_args():
    """
    Parses args.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--nb')

    global _args
    _args = parser.parse_args()


def analyse_results(config, stats):
    """
    Provides analysis of results
    :param config 
    :param stats
    """
    information = OrderedDict()
    df = pandas.DataFrame(list(map(lambda x: dict(x), stats))).fillna(0)
    for col in df.columns:
        for c in config.analysis.columns:
            if col.startswith(c.name):
                information[col] = c.operation(df[col])
    return OrderedDict(sorted(information.items(), key=lambda t: t[0]))


def main():
    stats = []
    config = Config().get_config()

    if _args.nb:
        config.games.number_of_games = _args.nb
    
    for _ in tqdm(range(int(config.games.number_of_games)), ascii=True, desc='Playing war games'):
        g = config.games.game_type(config)
        stats.append(g.play())

    for key, val in analyse_results(config, stats).items():
        print('{}: {}'.format(key, val))


if __name__ == '__main__':
    parse_args()
    main()