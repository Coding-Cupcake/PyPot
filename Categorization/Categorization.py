import os
import argparse
import math
import seaborn as sns

FEATURE = "6"

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("values", help="Please specify file containing the data points")
args = parser.parse_args()

# Open file and read data points
input_file = open(os.path.abspath(args.values), 'r')
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

result_data = []


range_bucket_f1 = 9612878/(math.pow(2, 10)-1)
range_bucket_f2 = 4979314/(math.pow(2, 10)-1)
range_bucket_f3 = 105/(math.pow(2, 10)-1)
range_bucket_f4 = 318112/(math.pow(2, 10)-1)
range_bucket_f5 = 677752/(math.pow(2, 10)-1)
range_bucket_f6 = 2619/(math.pow(2, 2)-1)
range_bucket_f7 = 12652/(math.pow(2, 10)-1)

for line in feature_values:

    if line[0] == "1":

        value = float((line[2:]))
        bucket = int(value/range_bucket_f1)
        if bucket > math.pow(2,9):
            category = 9
        else: category = int(math.log(bucket+1,2))
        result_data.append("1:" + str(category+1))

    elif line[0] == "2":
        value = float((line[2:]))
        bucket = int(value/range_bucket_f2)
        if bucket > math.pow(2,9):
            category = 9
        else: category = int(math.log(bucket+1,2))
        result_data.append("2:" + str(category+1))

    elif line[0] == "3":
        value = float((line[2:]))
        bucket = int(value/range_bucket_f3)
        if bucket > math.pow(2,9):
            category = 9
        else: category = int(math.log(bucket+1,2))
        result_data.append("3:" + str(category+1))

    elif line[0] == "4":
        value = float((line[2:]))
        bucket = int(value/range_bucket_f4)
        if bucket > math.pow(2,9):
            category = 9
        else: category = int(math.log(bucket+1,2))
        result_data.append("4:" + str(category+1))

    elif line[0] == "5":
        value = float((line[2:]))
        bucket = int(value/range_bucket_f5)
        if bucket > math.pow(2,9):
            category = 9
        else: category = int(math.log(bucket+1,2))
        result_data.append("5:" + str(category+1))

    elif line[0] == "6":
        value = float((line[2:]))
        bucket = int(value/range_bucket_f6)
        if bucket > math.pow(2,0):
            category = 1
        else: category = int(math.log(bucket+1,2))
        result_data.append("6:" + str(category+1))

    elif line[0] == "7":
        value = float((line[2:]))
        bucket = int(value/range_bucket_f7)
        if bucket > math.pow(2,9):
            category = 9
        else: category = int(math.log(bucket+1,2))
        result_data.append("7:" + str(category+1))

out_file = open("1_60_out", 'w')

f_1 = 0
f_2 = 1
f_3 = 2
f_4 = 3
f_5 = 4
f_6 = 5
f_7 = 6
i = 0

no_features = 7

out_result = []

while i < len(input_stats):
    result_string = input_stats[i][0:2] + result_data[f_1] + " " + result_data[f_2] + " " + result_data[f_3] + " " + result_data[f_4] + " " + result_data[f_5] + " " + result_data[f_6] + " " + result_data[f_7]
    out_result.append(result_string)
    i += 1
    f_1 += no_features
    f_2 += no_features
    f_3 += no_features
    f_4 += no_features
    f_5 += no_features
    f_6 += no_features
    f_7 += no_features
    print result_string

for element in out_result:
    out_file.write(element + '\n')


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


# Remove label
features_wo_label = []

for line in out_result:
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
    if line[0] == FEATURE:
        value = float(line[2:])
        feature_data.append(value)

bound = 1
bound_max = int(len(feature_data)*bound)

feature_data.sort()
plot_data = feature_data[0:bound_max]

print "Minimum: " + str(min(plot_data))
print "Maximum: " + str(max(plot_data)) + "\n"

#print "Remaining data: " + str(float(len(plot_data))/len(feature_data))


# Plot Histogram
sns.distplot(plot_data, kde=False)
sns.plt.xticks([1,2])
sns.plt.title(get_title(FEATURE))
sns.plt.show()