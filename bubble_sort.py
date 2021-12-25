import random

def create_random_numbers(size_of_array):
    numbers = []
    for i in range(size_of_array):
        numbers.append(random.randint(1,10000))
    return  numbers

def bubble_sort(unsorted_list):
    # Iterate through the list
    for i in range(len(unsorted_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(unsorted_list) - 1):
            if unsorted_list[j] > unsorted_list[j+1]:
                # Swap
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]



"""When no swaps are made --> list is sorted. Previously implemented algorithm, keep evaluating the rest of list even though its already sorted
FIX: boolean flag:  check if any swaps were made in previous iteration."""


def bubble_sort_optimized(unsorted_list):
    # stop passing through the list as soon as we pass through without swapping any
    has_swapped = True

    while(has_swapped):
        has_swapped = False
        for i in range(len(unsorted_list) - 1):
            if unsorted_list[i] > unsorted_list[i+1]:
                # Swap
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
                has_swapped = True

def main():
    unsorted = create_random_numbers(1000)
    bubble_sort(unsorted)
    print(unsorted)

    unsorted = create_random_numbers(1000)
    bubble_sort_optimized(unsorted)
    print(unsorted)

main()