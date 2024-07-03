def merge_sort(arr):
    """
    Recursively sorts an array using the merge sort algorithm.

    Args:
    arr (list): The list to be sorted.

    Returns:
    list: A sorted list.
    """
    if len(arr) <= 1:
        return arr
    
    # Divide the list into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves
    return merge_two_sorted_list(left, right)

def merge_two_sorted_list(a, b):
    """
    Merges two sorted lists into one sorted list.

    Args:
    a (list): The first sorted list.
    b (list): The second sorted list.

    Returns:
    list: A merged and sorted list.
    """
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    # Merge elements from both lists in sorted order
    while i < len_a and j < len_b:  # stop at the end of either list
        if a[i] < b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    
    # Append any remaining elements from list a
    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    
    # Append any remaining elements from list b
    while j < len_b:
        sorted_list.append(b[j])
        j += 1
    
    return sorted_list

if __name__ == '__main__':
    # Sample input list
    arr = [10, 3, 15, 7, 8, 23, 98, 29]
    # Print the sorted list
    print(merge_sort(arr))
