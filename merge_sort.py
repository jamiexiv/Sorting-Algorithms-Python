from RandomArrays import create_random_numbers

# Mergesort
# splits a list in half --> keeps splitting the list by 2 until it only has singular elements.
# Sorting is done by comparing the smallest elements of each half.
# Adjacent elements become sorted pairs, then sorted pairs are merged and sorted with other pairs as well.

# Recursive
# time complexity: O(nlog(n))


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # We use the list lengths often, so its handy to make variables
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if (left_list_index) < left_list_length and right_list_index < right_list_length:
            # we check which value from each list is smaller
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # if we reached end of the left list, add the elements from the right list
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

        # if we reached the end of the right list, add the elements from the left list
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    # use floor division to get midpart
    mid = len(nums) // 2

    # sort and merge each half
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)


def main():
    nums = create_random_numbers(100)
    nums = merge_sort(nums)
    print(nums)


main()

