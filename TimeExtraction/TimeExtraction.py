import os
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("buckets", help="Enter number of buckets")
args = parser.parse_args()

BUCKETS = int(args.buckets)

for in_file in os.listdir(os.curdir):

    if not in_file.endswith(".py") and not os.path.isdir(in_file):

        read_file = open(os.curdir + "/" + in_file, 'r')
        in_array = read_file.readlines()

        #out_array = []
        result_filtered = []

        index = 0
        second_index = 1
        steps = len(in_array)/BUCKETS

        while index < BUCKETS:

            #out_array.append("BUCKET " + str(index) + " : " + in_array[index*steps] + "  -  " + in_array[(second_index*steps)-1])
            #result_filtered.append(in_array[index*steps])
            result_filtered.append(in_array[(second_index*steps)-1])

            index += 1
            second_index += 1

        #out_file = open(os.curdir + "/" + in_file + "_out", 'w')
        out_filtered = open(os.curdir + "/" + in_file + "_out_records", 'w')

        #for row in out_array:
            #out_file.write(row)

        for row in result_filtered:
            out_filtered.write(row)

        print "Process finished for " + str(in_file)
