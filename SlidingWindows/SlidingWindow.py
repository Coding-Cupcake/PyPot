import os

WINDOW = 0.2
SLICE = 0.1

for f_ile in os.listdir(os.curdir):

    if f_ile.__contains__("test") or f_ile.__contains__("train"):
        in_file = open(os.curdir + "/" + f_ile, 'r')
        in_array = in_file.readlines()

        outer_dir = os.curdir + "/" + f_ile[0:5]

        if not os.path.exists(outer_dir):
                os.makedirs(outer_dir)

        num_records = len(in_array)
        window_size = int(num_records*WINDOW)
        slice_size = int(num_records*SLICE)

        start = 0
        stop = window_size

        index = 1

        while index < 10:

            print "START " + str(start)
            print "STOP " + str(stop)

            slice = in_array[start:stop]

            target_dir = outer_dir + "/" + str(index)

            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            out_file = open(target_dir + "/" + f_ile + "_" + str(index), 'w')

            for line in slice:
                out_file.write(line)

            start += slice_size
            stop += slice_size
            index += 1
