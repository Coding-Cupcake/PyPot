import os
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("window", help="Enter size of window in percent")
parser.add_argument("slice", help="Enter size of slide in percent")
parser.add_argument("buckets", help="Enter number of buckets")
args = parser.parse_args()

for test_file in os.listdir(os.curdir):

    if test_file.__contains__("test"):

        for train_file in os.listdir(os.curdir):

            if train_file.__contains__("train"):

                in_file_test = open(os.curdir + "/" + test_file, 'r')
                in_file_train = open(os.curdir + "/" + train_file, 'r')

                in_array_test = in_file_test.readlines()
                in_array_train = in_file_train.readlines()

                outer_dir = os.curdir + "/" + test_file[0:5]

                if not os.path.exists(outer_dir):
                        os.makedirs(outer_dir)

                WINDOW = float(args.window)
                SLICE = float(args.slice)
                BUCKETS = int(args.buckets)

                bucket_size_test = len(in_array_test)/BUCKETS
                num_records_train = len(in_array_train)
                window_size = int(num_records_train*WINDOW)
                slice_size = int(num_records_train*SLICE)

                start = 0
                stop = window_size

                index = int((WINDOW/SLICE) - 1)
                difference = index - 1

                while index < BUCKETS:

                    print "START " + str(start)
                    print "STOP " + str(stop)

                    slice = in_array_train[start:stop]

                    start_test = index * bucket_size_test
                    test_bucket = in_array_test[start_test:start_test + bucket_size_test]

                    target_dir = outer_dir + "/" + str(index-difference)

                    if not os.path.exists(target_dir):
                        os.makedirs(target_dir)

                    out_train = open(target_dir + "/" + train_file + "_" + str(index-difference), 'w')
                    out_test = open(target_dir + "/" + test_file + "_" + str(index-difference), 'w')

                    for line in slice:
                        out_train.write(line)

                    for other_line in test_bucket:
                        out_test.write(other_line)

                    start += slice_size
                    stop += slice_size
                    index += 1
