from RandomArrays import create_random_numbers

# segments list into 2 parts: unsorted and sorted
# continuously move the smallest item from unsorted list and append to sorted list
# Time complexity: O(n^2)

def selection_sort(nums):
    # i corresponds to how many items are sorted
    for i in range(len(nums)):
        lowest_value_index = i
        # j loops through the unsorted list
        for j in range(i+1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # swap values of lowest unsorted element with the first unsorted element
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]





def main():
    nums = create_random_numbers(10)
    print("Old array: " + str(nums))
    selection_sort(nums)
    print("New array: " + str(nums))


main()