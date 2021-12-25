from RandomArrays import create_random_numbers

# time complexity: O(n*log n)
# no additional memory
# binary heap
# segments the list into sorted and unsorted parts

# Step 1: convert list into binary heap tree
# Step 2: biggest element is the root node
# Step 3: place biggest element at the end of our list
# Step 4: rebuild heap tree which now has one less value
# Step 5: place the new largest value before the last item of our list
# Step 6: repeat until sorted


def heapify(nums, heap_size, root_index):
    # Assume that largest item is root index
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # If the left child of the root is a valid index, and the element is greater
    # than the current largest element, then update the largest element
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # Do the same for the right child of the root
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # If the largest element is no longer the root element, swap them
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # heapify the new root element to ensure its the largest
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)

    # create a max heap from the list
    # the 2nd argument of range means we stop at the element before -1 i.e.
    # the first element of the list
    # the 3rd argument of range means we iterate backwards, reducing the count
    # of i by 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # move the root of the max heap to the end of
    for i in range(n -1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

def main():
    nums = create_random_numbers(100000)
    print(nums)
    heap_sort(nums)
    print(nums)

main()