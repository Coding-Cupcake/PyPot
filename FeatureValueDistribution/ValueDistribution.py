import os
import argparse
import seaborn as sns

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("values", help="Please specify file containing the data points")
parser.add_argument("percentage", help="Please specify the percentage of data to be plotted")
parser.add_argument("feature", help="Please select the feature to be plotted")
args = parser.parse_args()

# Specify title of chart
def get_title(feature):
    if feature == "1":
        return "Average Number of Followers"
    if feature == "2":
        return "Audience Size Last Hour"
    if feature == "3":
        return "Duration/Retweet Ratio"
    if feature == "4":
        return "Time since last Retweet in Minutes"
    if feature == "5":
        return "Cut Duration in Minutes"
    if feature == "6":
        return "Retweet Count"
    if feature == "7":
        return "Cascade Duration in Hours"

# Open file and read data points
input_file  = open(os.path.abspath(args.values), 'r')
input_stats = input_file.readlines()

# Remove label
features_wo_label = []

for line in input_stats:
    features_wo_label.append(line[2:])

# Extract features
feature_values = []

for line in features_wo_label:
    temp = line.split(" ")
    for feature in temp:
        feature_values.append(feature)

# Extract feature values of concrete feature
feature_data = []
plot_data = []

for line in feature_values:
    if line[0] == args.feature:
        value = float(line[2:])
        feature_data.append(value)

bound = float(args.percentage)
bound_max = int(len(feature_data)*bound)

feature_data.sort()
plot_data = feature_data[0:bound_max]

print "Data Set: " + args.values + " - " + "Feature: " + args.feature
print "Minimum: " + str(min(plot_data))
print "Maximum: " + str(max(plot_data)) + "\n"

#print "Remaining data: " + str(float(len(plot_data))/len(feature_data))


# Plot Histogram
sns.distplot(plot_data, kde=False)
sns.plt.title(get_title(args.feature))
sns.plt.show()