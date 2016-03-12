import os
import calendar
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Enter the name of the libsvm training file")
args = parser.parse_args()

def toTimestamp(sTimestamp):
    """
    Takes a Unix or UTC timestamp as string. Returns the timestamp as
    a long in seconds.
    """
    lTimestamp = None
    try:
        lTimestamp = long(sTimestamp) / 1000 # Convert to seconds.
    except ValueError:
        lTimestamp = calendar.timegm(time.strptime(
            sTimestamp, "%a %b %d %H:%M:%S +0000 %Y"))
    return lTimestamp

for in_file in os.listdir(os.curdir):

    if not in_file.endswith(args.file) and not in_file.endswith(".py") and not os.path.isdir(os.curdir + "/" + in_file):
        input_file = open(in_file, 'r')
        in_data = input_file.read().split("\n")

        in_array = []
        for line in in_data:
            if len(line.strip()) > 0 and not line.startswith("Norm") and not line.startswith("Writ") and not line.startswith("Prod"):
                if line[0].isdigit():
                    in_array.append(line)
                else:
                    converted_ts = toTimestamp(line)
                    in_array.append(converted_ts)

        print len(in_array)
        outfile = open("out", 'w')
        out_array = []
        i = 0
        while i < len(in_array):
            out_array.append(str(in_array[i]))
            i += 1

        lib = open(args.file, 'r')
        lib_content = lib.readlines()
        result = []
        j = 0
        while j < len(lib_content):
            result.append(out_array[j] + " | " + lib_content[j])
            j += 1
        for line in result:
            outfile.write(line)
        outfile.close()
        final = open("out", 'r')
        final_arr = final.readlines()
        final_arr.sort()

        final_out = []
        for line in final_arr:
            final_out.append(line.split('|')[1].lstrip())

        final_sorted = open(args.file + "_sorted", 'w')
        for line in final_out:
            final_sorted.write(line)

        print final_arr
