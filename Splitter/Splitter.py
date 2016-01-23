
import os
import pickle

DIR = os.curdir
FOLDS = 10
LINE = "-----------------------------------"

j = 1

for pickle_file in os.listdir(DIR):

    i = 1
    if not os.path.isdir(pickle_file):
        if not pickle_file.endswith("X"):
            if not pickle_file.endswith(".py"):
                with open(pickle_file, 'rb') as p_file:
                    if not os.path.exists("_" + pickle_file):
                                os.makedirs("_" + pickle_file)
                    cv_list = pickle.load(p_file)
                    print LINE
                    print "Start processing for data set " + pickle_file
                    print LINE
                    lib_svm = open("lib_" + pickle_file + "X", 'r')
                    lib_list = lib_svm.readlines()
                    while i <= FOLDS:
                        print "------Create Fold " + str(i) + "------"
                        if not os.path.exists("_" + pickle_file + "/" + str(i)):
                                os.makedirs("_" + pickle_file + "/" + str(i))
                        train_out = open("_" + pickle_file + "/" + str(i) + "/" + pickle_file + "train_" + str(i), 'w')
                        test_out = open("_" + pickle_file + "/" + str(i) + "/" + pickle_file + "test_" + str(i), 'w')

                        train_array = []
                        test_array = []

                        for train_elem in cv_list[i-1][0]:
                            train_array.append(lib_list[train_elem])
                        for test_elem in cv_list[i-1][1]:
                            test_array.append(lib_list[test_elem])

                        for line in train_array:
                            for other_line in train_array:
                                if line[0] != other_line[0] and line[1:] == other_line[1:]:
                                    train_array.remove(other_line)
                                    print "Remove duplicate data point in training set: " + other_line

                        for line in test_array:
                            for other_line in test_array:
                                if line[0] != other_line[0] and line[1:] == other_line[1:]:
                                    test_array.remove(other_line)
                                    print "Remove duplicate data point in testing set: " + other_line

                        for line in train_array:
                            train_out.write(line)
                        for line in test_array:
                            test_out.write(line)

                        i += 1
                    print LINE
                    print "Processed folds for " + pickle_file
                    print LINE
                j += 1
print "Finished processing"
print "ALL FILES: " + str(j-1)


