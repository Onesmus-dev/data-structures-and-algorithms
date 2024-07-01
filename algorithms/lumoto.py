# Function to swap elements at indices a and b in array arr
def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]

# Function to perform Lomuto partition scheme
def lomutoPartition(elements, low, high):
    pivot = elements[high]  # Choose the last element as the pivot
    i = low - 1  # Index of smaller element

    # Loop through the array from low to high-1
    for j in range(low, high):
        if elements[j] <= pivot:  # If current element is smaller than or equal to pivot
            i += 1  # Increment the index of the smaller element
            swap(i, j, elements)  # Swap elements

    # Swap the pivot element with the element at i+1 position
    swap(i + 1, high, elements)
    return i + 1  # Return the partition index

# Function to perform Quick Sort using recursion
def quick_sort(elements, low, high):
    if low < high:
        # Partition the array and get the partition index
        pi = lomutoPartition(elements, low, high)
        
        # Recursively sort elements before and after partition
        quick_sort(elements, low, pi - 1)
        quick_sort(elements, pi + 1, high)

# Main block to test the Quick Sort implementation
if __name__ == '__main__':
    elements = [10, 7, 8, 9, 1, 5]
    quick_sort(elements, 0, len(elements) - 1)
    print("Sorted array is:", elements)
    tests = [
        [11, 9, 29, 27, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements) - 1)
        print(f'sorted array: {elements}')