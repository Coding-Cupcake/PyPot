import os
import argparse
import numpy as np

LINE = "----------------------------"

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("algorithm", help="Enter either 0 for MF or 1 for BSGD")
parser.add_argument("input_file", help="The file containing the statistics from the run")
args = parser.parse_args()

# Open file and read stats
input_file  = open(os.path.abspath(args.input_file), 'r')
input_stats = input_file.readlines()

# Check chosen algorithm
algorithm = args.algorithm
accuracy = []
time_execution  = []
time_prediction = []

# For Mondrian Forest
if algorithm == '0':
    for line in input_stats:
        for word in line.split():
            if word.__eq__("accuracy"):
                for number in line.split():
                    if number[0].isdigit():
                        accuracy.append(number)
            elif word.__eq__("executing"):
                for other in line.split():
                    if other.__eq__("Total"):
                        for number in line.split():
                            if number[0].isdigit():
                                time_execution.append(number)
            elif word.__eq__("prediction/evaluation"):
                for number in line.split():
                    if number[0].isdigit():
                        time_prediction.append(number)


# For Budgeted Stochastic Gradient Descent
if algorithm == '1':
    for line in input_stats:
        for word in line.split():
            if word.__eq__("error"):
                for number in line.split():
                    if number[0].isdigit():
                        accuracy.append(number)
            elif word.__eq__("Training"):
                for other in line.split():
                    if other.__eq__("completed"):
                        for number in line.split():
                            if number[0].isdigit():
                                time_execution.append(number)
            elif word.__eq__("Testing"):
                for other in line.split():
                    if other.__eq__("completed"):
                        for number in line.split():
                            if number[0].isdigit():
                                time_prediction.append(number)

accuracy_result = np.array(map(float, accuracy))
execution_result  = np.array(map(float, time_execution))
prediction_result = np.array(map(float, time_prediction))

if algorithm == '0':
    print LINE + "\n" + "Statistics for Mondrian Forest \n" + LINE
else:
    print LINE + "\n" + "Statistics for BSGD \n" + LINE

print "Average Accuracy: " + str(np.mean(accuracy_result))
print "Total execution time: " + str(np.sum(execution_result))
print "Total prediction time: " + str(np.sum(prediction_result))