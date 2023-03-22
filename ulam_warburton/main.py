# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math
import time
import os

b = 0


def make_next_log_folder():
    counter = open("counter.txt", 'r')
    n = int(counter.readline())
    counter.close()
    name = str(n) + "_logs/"
    os.makedirs(name)

    counter = open("counter.txt", 'w')
    counter.write(str(n + 1))
    counter.close()

    return name


def test_my_time(step):
    start = time.time()
    chess_method(step)
    return time.time() - start


def test_wiki_time(step):
    start = time.time()
    wiki_method(step)
    return time.time() - start


def test_chess_recursive_time(step):
    start = time.time()
    a = chess_method_recursive(step)
    return time.time() - start


def test_chess_inverted_time(step):
    start = time.time()
    chess_method_inverted(step)
    return time.time() - start


def test_chess_synthetic_time(step):
    start = time.time()
    chess_method_synthetic(step)
    return time.time() - start


def test_same_answer(n):
    for i in range(n):
        chess = chess_method(i + 1)
        assert math.ceil(wiki_method(i + 1)) == chess
        assert chess == chess_method_inverted(i + 1)
        assert chess == chess_method_recursive(i + 1)
        assert chess == chess_method_synthetic(i + 1)
    print("Passed! wiki_method, chess_method, chess_method_inverted, chess_method_synthetic, and chess_method_recursive"
          " return the same value for all numbers 1 to " +
          str(n) + ".")


def test_same_answer_specific(f1, f2, n):
    for i in range(n):
        assert f1(n) == f2(n)
    print("Passed! ")


def three_to_the(n):
    return 3 ** n


def wiki_method(x):
    i = 0
    out = 0
    while i <= x - 1:
        out += 3 ** hamming_weight(i)
        i += 1
    return 4 / 3 * out - 1 / 3


def chess_method(x):
    t1 = 4 ** math.floor(math.log2(x))
    t2 = math.floor((4 ** math.floor(math.log2(x))) / 3)

    acc = 0
    a = 0
    while a <= x - 2 ** math.floor(math.log2(x)) - 1:
        acc += 3 ** hamming_weight(a)
        a += 1

    t3 = 4 * acc
    return t1 + t2 + t3


def chess_method_inverted(x):
    t1 = 4 ** math.ceil(math.log2(x))
    t2 = math.floor((4 ** math.ceil(math.log2(x))) / 3)

    acc = 0
    a = x
    while a <= 2 ** math.ceil(math.log2(x)) - 1:
        acc += 3 ** (hamming_weight(a) - 1)
        a += 1

    t3 = 4 * acc
    return t1 + t2 - t3


def chess_method_synthetic(x):
    lower = 2 ** math.floor(math.log2(x))
    upper = 2 ** math.ceil(math.log2(x))
    if x > lower + (upper - lower) / 2:
        return chess_method_inverted(x)
    else:
        return chess_method(x)


def chess_method_recursive(x):
    if x == 0:
        return 0
    # t1 = 4 ** math.floor(math.log2(x))
    # t2 = math.floor((4 ** math.floor(math.log2(x))) / 3)
    t1 = (4 * 4 ** math.floor(math.log2(x)) - 1) // 3
    t2 = 0
    if math.log2(x) == math.floor(math.log2(x)):
        return t1 + t2
    t3 = 3 * (chess_method_recursive(x - 2 ** math.floor(math.log2(x)))) + 1

    return t1 + t2 + t3


def hamming_weight(x):
    if x == 0:
        return 0
    acc = 0
    k = 1
    while k <= math.log2(x):
        acc += math.floor(x / (2 ** k))
        k += 1
    return x - acc


def run_at_powers_2_standard_out():
    print("Warburton method at powers of 2, each line is the next power of two, starting from 0.")
    for i in range(10):
        print(test_wiki_time(2 ** (i + 1) - 1))

    print("My method at powers of 2, each line is the next power of two, starting from 0.")
    for i in range(10):
        print(test_my_time(2 ** (i + 1) - 1))


def run_standard_out():
    step_size = 1000
    step_number = 100

    print("Recursive Method")
    for i in range(step_number - 1):
        print(test_chess_recursive_time((i + 1) * step_size))
    print("######################################")
    print("Synthetic Method")
    for i in range(step_number - 1):
        print(test_chess_synthetic_time((i + 1) * step_size))


def backwards_standard_out():
    step_size = 1000
    step_number = 100

    print("Chess Method")
    for i in range(step_number - 1):
        print(test_my_time((i + 1) * step_size))

    print("######################################")

    print("Inverted Chess Method")
    for i in range(step_number - 1):
        print(test_chess_inverted_time((i + 1) * step_size))


def run_file_out():
    step_size = 1000
    step_number = 100
    dir_name = make_next_log_folder()

    wiki_logs = open(dir_name + "wiki_logs.txt", "a")
    wiki_logs.write("Warburton's method, each line contains the time it took in seconds for that method to produce a"
                    "result. First line is step " + str(step_size) + " second line is step " + str(
        step_size * 2) + " and"
                         " so on.\n")
    for i in range(step_number):
        wiki_logs.write(str(test_wiki_time((i + 1) * step_size)) + "\n")
    wiki_logs.close()

    chess_logs = open(dir_name + "chess_logs.txt", "a")
    chess_logs.write("Chess method, each line contains the time it took in seconds for that method to produce a"
                     "result. First line is step " + str(step_size) + " second line is step " + str(step_size * 2) +
                     " and so on.\n")
    for i in range(step_number):
        chess_logs.write(str(test_my_time((i + 1) * step_size)) + "\n")
    chess_logs.close()
    print("Finished, output in files wiki_logs.txt and chess_logs.txt.")


def run_file_out_all():
    step_size = 100000
    step_number = 10
    dir_name = make_next_log_folder()

    wiki_logs = open(dir_name + "wiki_logs.txt", "a")
    wiki_logs.write("Warburton's method, each line contains the time it took in seconds for that method to produce a"
                    "result. First line is step " + str(step_size) + " second line is step " + str(
        step_size * 2) + " and"
                         " so on.\n")
    for i in range(step_number):
        wiki_logs.write(str(test_wiki_time((i + 1) * step_size)) + "\n")
    wiki_logs.close()

    chess_logs = open(dir_name + "chess_logs.txt", "a")
    chess_logs.write("Chess method, each line contains the time it took in seconds for that method to produce a"
                     "result. First line is step " + str(step_size) + " second line is step " + str(step_size * 2) +
                     " and so on.\n")
    for i in range(step_number):
        chess_logs.write(str(test_my_time((i + 1) * step_size)) + "\n")
    chess_logs.close()

    inverted_logs = open(dir_name + "inverted_logs.txt", "a")
    inverted_logs.write("Inverted chess method, each line contains the time it took in seconds for that method to"
                        "produce a result. First line is step " + str(step_size) + " second line is step " +
                        str(step_size * 2) + " and so on.\n")
    for i in range(step_number):
        inverted_logs.write(str(test_chess_inverted_time((i + 1) * step_size)) + "\n")
    inverted_logs.close()

    synthetic_logs = open(dir_name + "synthetic_logs.txt", "a")
    synthetic_logs.write("Synthetic chess method, each line contains the time it took in seconds for that method to "
                         "produce a result. First line is step " + str(step_size) + " second line is step " +
                         str(step_size * 2) + " and so on.\n")
    for i in range(step_number):
        synthetic_logs.write(str(test_chess_synthetic_time((i + 1) * step_size)) + "\n")
    synthetic_logs.close()

    recursive_logs = open(dir_name + "recursive_logs.txt", "a")
    recursive_logs.write("Recursive chess method, each line contains the time it took in seconds for that method to "
                         "produce a result. First line is step " + str(step_size) + " second line is step " +
                         str(step_size * 2) + " and so on.\n")
    for i in range(step_number):
        recursive_logs.write(str(test_chess_recursive_time((i + 1) * step_size)) + "\n")
    recursive_logs.close()

    print("Finished, output in files wiki_logs.txt, chess_logs.txt, inverted_logs.txt, synthetic_logs.txt,"
          " and recursive_logs.txt.")


if __name__ == '__main__':
    test_same_answer_specific(chess_method_synthetic, chess_method_recursive, 10000)
