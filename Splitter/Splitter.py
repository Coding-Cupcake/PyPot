
import os
import pickle

DIR = os.curdir
FOLDS = 10

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
                    print cv_list[0][1]
                    lib_svm = open("lib_" + pickle_file + "X", 'r')
                    lib_list = lib_svm.readlines()
                    while i <= FOLDS:
                        if not os.path.exists("_" + pickle_file + "/" + str(i)):
                                os.makedirs("_" + pickle_file + "/" + str(i))
                        train_out = open("_" + pickle_file + "/" + str(i) + "/" + pickle_file + "train_" + str(i), 'w')
                        test_out = open("_" + pickle_file + "/" + str(i) + "/" + pickle_file + "test_" + str(i), 'w')
                        for train_elem in cv_list[i-1][0]:
                            train_out.write(lib_list[train_elem])
                        for test_elem in cv_list[i-1][1]:
                            test_out.write(lib_list[test_elem])
                        i += 1
                j += 1
print "ALL FILES: " + str(j-1)