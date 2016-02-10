import os

HOME = os.curdir
OUTPUT = os.curdir + "/data"

for sorted_file in os.listdir(HOME):

    if not sorted_file.endswith(".py") and not os.path.isdir(HOME + "/" + sorted_file):

        sorted_input = open(HOME + "/" + sorted_file, 'r')
        sorted_array = sorted_input.readlines()

        for record in sorted_array:

            for other_record in sorted_array:

                if record[0] != other_record[0] and record[1:] == other_record[1:]:

                    print record[1:]
                    sorted_array.remove(record)

        sorted_output = open(OUTPUT + "/" + sorted_file + "_filtered", 'w')

        for line in sorted_array:

            sorted_output.write(line)
