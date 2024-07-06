def selection_sort(arr):
    """
    Sorts an array in ascending order using the selection sort algorithm.

    Args:
        arr (list): The list to be sorted.

    Returns:
        None (sorts the input list in-place)
    """

    size = len(arr)

    # Outer loop iterates through each element of the list (except the last)
    for i in range(size - 1):
        # Assume the first element in the unsorted part is the minimum
        min_index = i

        # Inner loop finds the actual minimum element in the unsorted part
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j

        # If the minimum element is not in its correct position, swap it
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [78, 12, 15, 8, 61, 53, 23, 27],
        [5]
    ]

    for elements in tests:
        selection_sort(elements)
        print(elements)
