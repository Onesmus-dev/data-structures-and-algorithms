# Function to swap elements at indices a and b in array arr
def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]

# Function to partition the array and return the partition index
def partition(elements, start, end):
    pivot_index = start  # Choosing the first element as the pivot
    pivot = elements[pivot_index]

    start = pivot_index + 1
    end = len(elements) - 1

    # Rearrange elements around the pivot
    while start < end:
        # Move start index forward while elements are less than or equal to the pivot
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        # Move end index backward while elements are greater than the pivot
        while elements[end] > pivot:
            end -= 1

        # Swap elements at start and end if start is still less than end
        if start < end:
            swap(start, end, elements)

    # Swap the pivot element with the element at the end index
    swap(pivot_index, end, elements)

    return end  # Return the index of the pivot element after partitioning

# Function to perform Quick Sort
def quick_sort(elements, start, end):
    if start < end:
        # Partition the array and get the partition index
        pi = partition(elements, start, end)
        # Recursively sort the elements before and after partition
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)

if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    tests = [
        [11, 9, 29, 27, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    # Run Quick Sort on each test case
    for elements in tests:
        quick_sort(elements, 0, len(elements) - 1)
        print(f'sorted array: {elements}')

    # Run Quick Sort on the initial elements array and print the result
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)
