import os

DATA_DIR = os.curdir + "/data/"
LINE = "---------------------"

true_positive = 0
false_negative = 0
true_negative = 0
false_positive = 0

for folder in os.listdir(DATA_DIR):
        true_positive = 0
        true_negative = 0
        false_negative = 0
        false_positive = 0
        cur_dir = DATA_DIR + folder + "/"
        for sub_folder in os.listdir(cur_dir):
            fin_dir = cur_dir + sub_folder + "/"
            for fi_le in os.listdir(fin_dir):
                name = os.path.splitext(fin_dir+fi_le)[0]
                if name.__contains__("Prediction"):
                    pred_file = open(fin_dir + fi_le, 'r')
                    pred_list = []
                    for line in pred_file:
                        pred_list.append(line[0])

                elif name.__contains__("test"):
                    test_file = open(fin_dir + fi_le,'r')
                    test_list = []
                    for line in test_file:
                        test_list.append(line[0])


            i = 0
            while i < len(pred_list):
                if pred_list[i] == str(1) and test_list[i] == str(1):
                    true_positive += 1
                elif pred_list[i] == str(0) and test_list[i] == str(0):
                    true_negative += 1
                elif pred_list[i] == str(0) and test_list[i] == str(1):
                    false_negative += 1
                elif pred_list[i] == str(1) and test_list[i] == str(0):
                    false_positive += 1
                i += 1

            print LINE
            print "Dataset: " + str(fi_le)
            print LINE
            print "True Positive: " + str(true_positive)
            print "True Negative: " + str(true_negative)
            print "False Positive: " + str(false_positive)
            print "False Negative: " + str(false_negative)






