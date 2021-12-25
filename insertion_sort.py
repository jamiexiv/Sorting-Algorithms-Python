from RandomArrays import create_random_numbers

# Like Selection Sort, this algorithm segments the list into sorted and unsorted parts.
# It iterates over the unsorted segment, and inserts the element being viewed into the correct position of the sorted list.

def insertion_sort(nums):
    # start at the second element
    for i in range (1, len(nums)):
        item_to_insert = nums[i]
        # keep a reference of the index of the previous element
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j+1] = nums[j]
            j -= 1
        # insert the item
        nums[j+1] = item_to_insert


# time complexity: O(n^2)


def main():
    nums = create_random_numbers(10)
    print("Old array: " + str(nums))
    insertion_sort(nums)
    print("New array: " + str(nums))

main()