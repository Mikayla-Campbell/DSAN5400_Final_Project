import argparse
from pprint import pprint
import logging
from matcher import Matcher
from pathlib import Path

def process_tsv(filepath):
    abstract_list = []
    project_root = Path(__file__).resolve().parent.parent
    data_dir = project_root / "data"
    for file_path in data_dir.glob("*.tsv"):
        with file_path.open("r", encoding="utf-8") as f:
            ...

    with open(filepath, 'r', encoding='utf-8') as f:
        for abstract in f:
            abstract_list.append(abstract.strip())
    return abstract_list

if __name__ == '__main__':
    # configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        filename='../../logs.txt')

    # import files
    october = '../data/2410oct.tsv'
    november = '../data/2411nov.tsv'
    december = '../data/2412dec.tsv'
    january = '../data/2501jan.tsv'
    february = '../data/2502feb.tsv'
    march = '../data/2503mar.tsv'

    abstracts_oct = process_tsv(october)
    abstracts_nov = process_tsv(november)
    abstracts_dec = process_tsv(december)
    abstracts_jan = process_tsv(january)
    abstracts_feb = process_tsv(february)
    abstracts_mar = process_tsv(march)

    # filter user request by argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--category', type=str, required=True, help='Category to match')
    parser.add_argument('-g', '--graph', action='store_true', required=False, help='Flag to display graph')

    args = parser.parse_args()
    category = args.category
    graph = args.graph

    # create matcher object
    matcher = Matcher(abstracts_oct, abstracts_nov, abstracts_dec,
                      abstracts_jan, abstracts_feb, abstracts_mar)

    print()
    print("Thank you for using the dei frequency matcher")
    print("Matched on category:", category)
    print("Here are your results:")
    pprint(matcher.match(category, graph), sort_dicts=False)