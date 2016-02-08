import os

HOME = os.curdir

for sorted_filed in os.listdir(HOME):
    if not sorted_filed.endswith(".py") and not os.path.isdir(HOME + "/" + sorted_filed):
        sorted_input = open(HOME + "/" + sorted_filed, 'r')
        sorted_array = sorted_input.readlines()
        for folder in os.listdir(HOME):

            print "Start processing: " + folder
            folder_dir = HOME + "/" + folder
            if os.path.isdir(folder_dir) and sorted_filed.__contains__(folder):
                for sub_folder in os.listdir(folder_dir):
                    sub_folder_dir = folder_dir + "/" + sub_folder
                    if os.path.isdir(sub_folder_dir):
                        for test_file in os.listdir(sub_folder_dir):
                            if test_file.__contains__("test"):
                                t_file = open(sub_folder_dir + "/" + test_file, 'r')
                                t_array = t_file.readlines()

                                t_array_ts = []

                                for record in t_array:
                                    for line in sorted_array:
                                        if record.__eq__(line.split('|')[1].lstrip()):
                                            t_array_ts.append(line)
                                            break

                                result_file = open(sub_folder_dir + "/" + test_file, 'w')
                                t_array_ts.sort()

                                print "Processing file: " + test_file

                                for line in t_array_ts:
                                    result_file.write(line.split('|')[1].lstrip())


