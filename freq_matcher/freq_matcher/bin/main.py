import argparse
from pprint import pprint
import logging
from freq_matcher.freq_matcher import Matcher
from utility.Process_data import download_data

def process_tsv(filepath):
    abstract_list = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for abstract in f:
            abstract_list.append(abstract.strip())
    return abstract_list

if __name__ == '__main__':
    # configure logging
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        filename='../../logs.txt')
    logging.info("Entered main.")

    # import files
    october_url = 'https://drive.google.com/uc?export=download&id=15O5--LaJl3S3nIJ00EpDCr0oNh8UiZDi'
    november_url = 'https://drive.google.com/uc?export=download&id=1PIsMTxY5zmTEjU73dII07XGdCG7J2FhE'
    december_url = ' https://drive.google.com/uc?export=download&id=1H2mPOoQvOdHgb1176ieZHAoUrhIVYa-5'
    january_url = 'https://drive.google.com/uc?export=download&id=1ZrwmQ8KwebNkni-fnguRiUfKq_n0tce_'
    february_url = ' https://drive.google.com/uc?export=download&id=1IXGPA0K_A038DAeIFCvTy2eJNH599XOj'
    march_url = 'https://drive.google.com/uc?export=download&id=1i0VVWp4lSswgNb3227LvDOtFEHaKDZ-s'

    download_data(october_url, '../../data/2410oct.tsv')
    download_data(november_url, '../../data/2411nov.tsv')
    download_data(december_url, '../../data/2412dec.tsv')
    download_data(january_url, '../../data/2501jan.tsv')
    download_data(february_url, '../../data/2502feb.tsv')
    download_data(march_url, '../../data/2503mar.tsv')

    october = '../../data/2410oct.tsv'
    november = '../../data/2411nov.tsv'
    december = '../../data/2412dec.tsv'
    january = '../../data/2501jan.tsv'
    february = '../../data/2502feb.tsv'
    march = '../../data/2503mar.tsv'

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

    #create matcher object
    matcher = Matcher(abstracts_oct, abstracts_nov, abstracts_dec,
                    abstracts_jan, abstracts_feb, abstracts_mar)

    print()
    print("Thank you for using the dei frequency matcher")
    print("Matched on category:", category)
    print("Here are your results:")
    pprint(matcher.match(category, graph), sort_dicts=False)



