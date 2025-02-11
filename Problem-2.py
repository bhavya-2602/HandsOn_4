def remove_duplicates(array):
    """Removes duplicate elements from a given array while maintaining order."""
    if not array:
        return []  # Return an empty list if the input array is empty
    
    unique_list = []  # List to store unique elements
    seen = set()  # Set to keep track of seen elements
    
    for num in array:
        if num not in seen:  # If the number is not in seen set, add it
            unique_list.append(num)
            seen.add(num)
    
    return unique_list  # Return the list with duplicates removed

if __name__ == "__main__":
    # Example test cases
    array1 = [2, 2, 2, 2, 2]  # All elements are duplicates
    array2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]  # Mixed unique and duplicate elements

    # Print results after removing duplicates
    print("Array after removing duplicates:", *remove_duplicates(array1))
    print("Array after removing duplicates:", *remove_duplicates(array2))
