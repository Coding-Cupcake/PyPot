import pickle
import os

# Input data path
INPUT = os.curdir + "/data/"
LINE = "-----------------------------"


# Extract number
def extract_number(pickle_file):
    i = 0
    while pickle_file[i].isdigit():
        i += 1
    return pickle_file[0:i]


# List builder function
def list_builder(predictions, real_values):
    tree_prediction_stats = pickle.load(open(predictions, 'r'))
    real_values = open(real_values, 'r')

    prediction_values = []
    for row in tree_prediction_stats['pred_prob_overall_test']:
        if max(row[0], row[1]) == row[0]:
            prediction_values.append('0')
        else:
            prediction_values.append('1')

    test_values = []
    for line in real_values:
        test_values.append(line[0])

    return prediction_values, test_values

# Check all tree predictions
for folder in os.listdir(INPUT):

    true_positive = 0
    true_negative= 0
    false_positive = 0
    false_negative= 0

    if os.path.isdir(INPUT + folder):
        cur_dir = INPUT + folder + "/"
        for p_file in os.listdir(cur_dir):
            if p_file.endswith('predictions.p'):
                pred_values = []
                act_values = []
                number = extract_number(p_file)
                for test_file in os.listdir(cur_dir):
                    if test_file.endswith(number):
                        pred_values, act_values = list_builder(cur_dir + p_file, cur_dir + test_file)
                        break
                i = 0
                while i < len(pred_values):
                    if pred_values[i] == str(1) and act_values[i] == str(1):
                        true_positive += 1
                    elif pred_values[i] == str(0) and act_values[i] == str(0):
                        true_negative += 1
                    elif pred_values[i] == str(0) and act_values[i] == str(1):
                        false_negative += 1
                    elif pred_values[i] == str(1) and act_values[i] == str(0):
                        false_positive += 1
                    i += 1

        print LINE
        print "Dataset: " + str(folder)
        print LINE
        print "True Positive: " + str(true_positive)
        print "True Negative: " + str(true_negative)
        print "False Positive: " + str(false_positive)
        print "False Negative: " + str(false_negative)