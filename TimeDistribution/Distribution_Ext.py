import os
import argparse
import datetime
import numpy as np
import matplotlib.pyplot as plt
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

        # Check for the timestamp of the original message
        if words[index].__contains__("created_at"):

            if words[index][13:].__contains__("\""):  # Format: Fri Aug 03 15:10:58 +0000 2012
                ts_array.append(datetime.datetime.fromtimestamp(toTimestamp(words[index][14:-1])).strftime('%d-%m-%Y'))

            else:  # Format: 1344006622000
                ts_array.append(datetime.datetime.fromtimestamp(int(words[index][13:-1])/100).strftime('%d-%m-%Y'))
            break
        else:
            index += 1

# Cut for plotting
ts_array_cut = []

for date in ts_array:
    ts_array_cut.append(date[0:5])

# Work with set
ts_set = set(ts_array)
out_sorted = []

for line in ts_set:
    n = ts_array.count(line)
    out_sorted.append(line + "," + str((n/float(len(ts_array)))*100) + "," + str(n))
out_sorted.sort(key = lambda x: x.split(',')[0], reverse=False)

# Convert timestamp array to dictionary
timestamps = dict((x, ts_array_cut.count(x)) for x in ts_array_cut)

# Get the heights and labels from the dictionary
heights, labels = [], []
for key, val in timestamps.iteritems():
    labels.append(key)
    heights.append(val)

# Create a set of fake indexes at which to place the bars
indexes = np.arange(len(timestamps))
width = 0.4

# Generate a matplotlib figure and plot the bar chart
fig, ax = plt.subplots()
ax.bar(indexes, heights)

# Overwrite the axis labels
ax.set_xticks(indexes + width)
ax.set_xticklabels(labels, rotation='vertical')

# Plot chart
plt.show()

# Print out_sorted
for line in out_sorted:
    print line
