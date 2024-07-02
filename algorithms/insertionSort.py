def insertion_sort(elements):
    """
    Sorts a list of elements in ascending order using the insertion sort algorithm.

    Insertion sort works by iteratively building a sorted sub-list at the beginning of the input list.
    For each element in the unsorted sub-list, it compares with the elements in the sorted sub-list
    and inserts it at the correct position to maintain the sorted order.

    Args:
        elements (list): The list of elements to be sorted.

    Returns:
        list: The sorted list. (Note: In Python, functions don't modify the original list,
              they return a new sorted list.)
    """

    for i in range(1, len(elements)):
        """
        Iterate through the unsorted sub-list starting from the second element (index 1).
        """
        anchor = elements[i]
        """
        Extract the current element (anchor) for comparison and insertion.
        """
        j = i - 1
        """
        Initialize the index 'j' to point to the element before the current one
        in the sorted sub-list.
        """
        while j >= 0 and anchor < elements[j]:
            """
            Shift elements in the sorted sub-list to the right
            until the correct position for the 'anchor' is found.
            """
            elements[j + 1] = elements[j]
            j -= 1

        elements[j + 1] = anchor
        """
        Insert the 'anchor' element at its correct position in the sorted sub-list.
        """

    return elements  # Return the sorted list

if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    sorted_elements = insertion_sort(elements)
    print(sorted_elements)  # Print the sorted list
