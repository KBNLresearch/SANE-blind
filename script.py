from glob import glob
import re
import csv
import collections #bevat ook counter om tokens te tellen (kan ook: from collections import Counter)

input_path="/home/sara/Dataservices/SANE/text-out-CB/"
#input_path="/input" #voor testen Karina outcommenten
filepaths=glob(f"{input_path}*.txt")
frequency_lists={}
for filepath in filepaths:
    with open(filepath,"r", encoding="utf-8") as textfile:
        text=textfile.read()
        text=text.lower()
        text=re.sub("[\.,\'\":;\?\!\(\)]+","",text) #check in tests of deze volledig is
        tokens=text.split()
        frequencies=collections.Counter(tokens)
        frequency_lists[filepath]=frequencies.most_common()

output_path="/home/sara/Dataservices/SANE/testoutput/"
#output_path="/output" #voor testen Karina outcommenten
for filename, frequencies in frequency_lists.items():
    filename=filename.split("\\")[-1]
    filename=output_path+filename.replace(".txt", ".csv")
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer=csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(frequencies)
