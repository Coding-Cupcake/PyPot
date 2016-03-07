import os
import argparse
import datetime

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("ts_file", help="Please specify file containing time stamps for data points")
args = parser.parse_args()

# Open file and read data points
input_file  = open(os.path.abspath(args.ts_file), 'r')
input_stats = input_file.readlines()

# Extract time stamps
ts_array = []
ts_array_converted = []

for line in input_stats:
    ts_array.append(line[0:10])

for line in ts_array:
    ts_array_converted.append(datetime.datetime.fromtimestamp(int(line)).strftime('%d-%m-%Y'))

# Work with set
ts_set = set(ts_array_converted)
out_sorted = []

for line in ts_set:
    n = ts_array_converted.count(line)
    out_sorted.append(line + "," + str((n/float(len(ts_array_converted)))*100) + "," + str(n))
out_sorted.sort(key = lambda x: x.split(',')[1], reverse=True)
#print out_sorted
for line in out_sorted:
    print line
