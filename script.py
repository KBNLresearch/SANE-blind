from glob import glob
import argparse
import re
import csv
import collections #bevat ook counter om tokens te tellen (kan ook: from collections import Counter)

def process_input(input_path):
    filepaths = glob(f"{input_path}*.txt")
    frequency_lists = {}
    for filepath in filepaths:
        with open(filepath, "r", encoding="utf-8") as textfile:
            text = textfile.read()
            text = text.lower()
            text = re.sub("[\.,\'\":;\?\!\(\)]+", "", text)  # check in tests of deze volledig is
            tokens = text.split()
            frequencies = collections.Counter(tokens)
            frequency_lists[filepath] = frequencies.most_common()
    return frequency_lists

def output_results(frequency_lists, output_path):
    for filename, frequencies in frequency_lists.items():
        filename = filename.split("\\")[-1].split('/')[-1]
        filename = output_path + filename.replace(".txt", ".csv")
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
            writer.writerows(frequencies)

if __name__ == '__main__':
    '''
    Rewrote Karina's script to work in the SANE environment
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path', help='input folder', required=True)
    parser.add_argument('-o', '--output_path', help='output folder', required=True)
    parser.add_argument('-t', '--temp', help='temp folder', required=True)

    args = parser.parse_args()
    print(f'Going to process {args.input_path} and write results to {args.output_path}')
    frequency_lists = process_input(args.input_path)
    output_results(frequency_lists, args.output_path)
