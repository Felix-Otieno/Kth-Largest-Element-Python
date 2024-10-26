def largest_element(digits, K):
    """
    A function that is task is to find the Kth largest element in the unsorted list.
    It takes two parameters: digits, the unsorted list
                             K, the rank of the targeted largest element in unsorted list
    """
    # Sort the list in descending order(Largest to smallest)
    # By default the sorted() sorts the list in ascending order and the parameter reverse=True used to specify in descending order
    sorted_list = sorted(digits, reverse=True)
    
    # It returns the Kth largest element in the sorted list.
    # K - 1 is the index of the targeted largest element in the sorted list because indexing starts at 0 in the lists. 
    return sorted_list[K-1]

# List of unsorted numbers
digits = [45, 20, 97, 15, 70, 69, 32, 88, 45]

# Rank of the Kth largest element in the list
K = 1

# Invoke the function to display the Kth largest element.
print(largest_element(digits, K))