import os
import argparse
import datetime
from Utils import toTimestamp

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("cascades_folder", help="Please specify folder containing cascades")
args = parser.parse_args()

ts_array = []

# Go through all cascades
for cascade in os.listdir(args.cascades_folder):
    input_file  = open(args.cascades_folder + "/" + cascade, 'r')
    input_stats = input_file.read()

    words = input_stats.split(',')
    index = 0

    while index < len(words):

        if words[index].__contains__("created_at"):
            if words[index][13:].__contains__("\""):
                ts_array.append(datetime.datetime.fromtimestamp(toTimestamp(words[index][14:-1])).strftime('%d-%m-%Y'))
            else:
                ts_array.append(datetime.datetime.fromtimestamp(int(words[index][13:23])).strftime('%d-%m-%Y'))
            break
        else:
            index += 1

# Work with set
ts_set = set(ts_array)
out_sorted = []

for line in ts_set:
    n = ts_array.count(line)
    out_sorted.append(line + "," + str((n/float(len(ts_array)))*100) + "," + str(n))
out_sorted.sort(key = lambda x: x.split(',')[1], reverse=True)

# Print out_sorted
for line in out_sorted:
    print line
