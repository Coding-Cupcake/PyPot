import os
import datetime
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("ts_file", help="Enter name of time stamp file (e.g. 1_60_TS)")
args = parser.parse_args()

# To use if there is a Time Stamp file

for in_file in os.listdir(os.curdir):

    if not os.path.isdir(in_file) and in_file.__contains__("records"):

        read_file = open(os.curdir + "/" + in_file, 'r')
        read_ts_file = open(os.curdir + "/" + args.ts_file, 'r')

        in_records = read_file.readlines()
        in_ts_records = read_ts_file.readlines()

        result = []
        result_final = []

        for record in in_records:

            for other_record in in_ts_records:

                if record == other_record.split("|")[1][1:]:

                    result.append(other_record)

        for result_record in result:

            if result_record[0] == "1":

                unix_ts = result_record.split("|")[0][0:10]
                record = result_record.split("|")[1]

                unix_ts_converted = datetime.datetime.fromtimestamp(int(unix_ts)).strftime('%d-%m-%Y')

                result_final.append(str(unix_ts_converted) + " --- " + record)

        out = open(os.curdir + "/" + args.ts_file + "_time_stamps" , 'w')

        for record in result_final:

            out.write(record)
