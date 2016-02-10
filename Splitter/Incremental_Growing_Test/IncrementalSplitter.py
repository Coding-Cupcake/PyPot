import os

# Creates buckets for simulating incremental learning.
# Test set size increases linearly with train size.

HOME = os.curdir
BUCKETS = 10    # Number
TEST_SIZE = 10  # Percent

for sorted_file in os.listdir(HOME):

    if not sorted_file.endswith(".py") and not os.path.isdir(HOME + "/" + sorted_file):

        os.makedirs(HOME + "/" + sorted_file + "X")
        sorted_input = open(HOME + "/" + sorted_file, 'r')
        sorted_array = sorted_input.readlines()

        index = 1
        bucket_percent = BUCKETS/float(100)

        while index <= BUCKETS:

            current_dir = HOME + "/" + sorted_file + "X" + "/" + str(index)
            os.makedirs(current_dir)

            bucket_size = int(len(sorted_array)*bucket_percent)
            bucket_size_train = int(((100-TEST_SIZE)/float(100))*bucket_size)
            bucket = sorted_array[0:bucket_size]

            train_set = bucket[0:bucket_size_train]
            test_set = bucket[bucket_size_train:]

            train_file = open(current_dir + "/" + sorted_file + "train_" + str(index), 'w')
            for train_record in train_set:
                train_file.write(train_record)

            test_file = open(current_dir + "/" + sorted_file + "test_" + str(index), 'w')
            for test_record in test_set:
                test_file.write(test_record)

            index += 1
            bucket_percent += BUCKETS/float(100)

