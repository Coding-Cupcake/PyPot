import os

# Creates a train and test set preserving temporal order.
# To be used as input for mondrian forest.

HOME = os.curdir
BUCKETS = 10    # Number
TEST_SIZE = 110  # E.g. 110 = No. train (10/11) : No. test (1/11) = 10 : 1

for sorted_file in os.listdir(HOME):

    if not sorted_file.endswith(".py") and not os.path.isdir(HOME + "/" + sorted_file):

        os.makedirs(HOME + "/" + sorted_file + "X")
        sorted_input = open(HOME + "/" + sorted_file, 'r')
        sorted_array = sorted_input.readlines()

        # Size of one test record bucket
        test_size = len(sorted_array)/TEST_SIZE

        index = 1
        bucket_percent = BUCKETS/float(100)

        current_dir = HOME + "/" + sorted_file + "X"

        train_set = []
        test_set = []

        start_pos = 0

        while index <= BUCKETS:

            bucket_size = int(len(sorted_array)*bucket_percent)
            bucket_size_train = bucket_size - test_size

            train_set_temp = sorted_array[start_pos:start_pos + bucket_size_train]
            test_set_temp = sorted_array[start_pos + bucket_size_train:start_pos + bucket_size_train + test_size]

            for train_record in train_set_temp:
                train_set.append(train_record)

            for test_record in test_set_temp:
                test_set.append(test_record)

            index += 1
            start_pos += bucket_size

        train_file = open(current_dir + "/" + sorted_file + "train" , 'w')
        for train_record in train_set:
            train_file.write(train_record)
        test_file = open(current_dir + "/" + sorted_file + "test", 'w')
        for test_record in test_set:
                test_file.write(test_record)
