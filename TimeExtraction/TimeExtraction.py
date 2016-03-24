import os

BUCKETS = 10

for in_file in os.listdir(os.curdir):

    if not in_file.endswith(".py") and not os.path.isdir(in_file):

        read_file = open(os.curdir + "/" + in_file, 'r')
        in_array = read_file.readlines()

        out_array = []

        index = 0
        second_index = 1
        steps = len(in_array)/BUCKETS

        while index < BUCKETS:

            out_array.append("BUCKET " + str(index) + " : " + in_array[index*steps] + "  -  " + in_array[(second_index*steps)-1])

            index += 1
            second_index += 1

        out_file = open(os.curdir + "/" + in_file + "_out", 'w')

        for row in out_array:
            out_file.write(row)

        print "Process finished for " + str(in_file)