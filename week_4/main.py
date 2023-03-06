import random
import statistics
import sys


def run_week_4_libraries():
    print("----- Week_4 Libraries -----")
    name_tags()


def find_mean():
    nums = list(range(10))
    print(statistics.mean(nums))


def shuffle_list():
    nums = list(range(10))
    random.shuffle(nums)
    print(nums)


def get_args():
    args = sys.argv
    if len(args) < 2:
        sys.exit("Too few arguments")
    elif len(args) > 2:
        sys.exit("Too many arguments")
    print("Hello, my name is", args[1])


def name_tags():
    args = sys.argv
    for name in args[1:]:
        print("Hello, my name is", name)


run_week_4_libraries()
