# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 7/08/2022
# Description: Uses a bubble sort and an insertion sort to sort a list and returns tuples of comparisons and
#               exchanges made during each respective sort.

def bubble_count(list):
    """Bubble sorts a list and returns a tuple of the comparisons and exchanges made."""

    comparisons = 0
    exchanges = 0

    for pass_num in range(len(list) - 1):

        for index in range(len(list) - 1 - pass_num):

            if list[index] > list[index + 1]:

                temp = list[index]

                list[index] = list[index + 1]

                list[index + 1] = temp

                exchanges += 1

            comparisons += 1

            print(list)

    comp_ex_tuple = (comparisons, exchanges)

    return comp_ex_tuple


def insertion_count(list):
    """Insertion sorts a list and returns a tuple of the comparisons and echanges made."""

    comparisons = 0
    exchanges = 0

    for index in range(1, len(list)):

        value = list[index]
        pos = index - 1

        while pos >= 0 and list[pos] > value:

            list[pos + 1] = list[pos]
            pos -= 1

            exchanges += 1

            comparisons += 1

        list[pos + 1] = value

        comparisons += 1

    comp_ex_tuple = (comparisons, exchanges)

    return comp_ex_tuple