import os
import datetime
from Utils import toTimestamp

# To use if there is no TS file (currently for the 1_100 data sets)

for in_file in os.listdir(os.curdir):

    if not os.path.isdir(in_file) and in_file.__contains__("records"):

        read_file = open(os.curdir + "/" + in_file, 'r')
        read_ts_file = open(os.curdir + "/" + "1_100_12000_clean.txt", 'r')
        read_all = open(os.curdir + "/" + "trainingdataset_1_100_LibSVM_sorted_filteredtrain", 'r')

        in_records = read_file.readlines()
        in_ts_records = read_ts_file.readlines()
        in_all_records = read_all.readlines()

        result = []
        result_final = []

        for record in in_records:

            line_count = 0

            for other_record in in_all_records:

                if record == other_record:

                    result.append(in_ts_records[line_count][:-1] + "|" + record)
                    break

                else:

                    line_count += 1

        for result_record in result:

            if result_record[0] == "1":  # Format: 1344006622000

                unix_ts = result_record.split("|")[0][0:10]
                record = result_record.split("|")[1]

                unix_ts_converted = datetime.datetime.fromtimestamp(int(unix_ts)).strftime('%d-%m-%Y')

                result_final.append(str(unix_ts_converted) + " --- " + record)

            else:  # Format: Fri Aug 03 15:10:58 +0000 2012

                result_final.append(result_record)

        out = open(os.curdir + "/" + "1_100_time_stamps" , 'w')

        for record in result_final:

            out.write(record)