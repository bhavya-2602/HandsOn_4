import heapq

def merge_k_sorted_arrays(arrays):
    min_heap = []
    
    # Initialize the heap with the first element of each array along with its index
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))
    
    merged = []
    
    # Process the heap until it's empty
    while min_heap:
        val, arr_idx, elem_idx = heapq.heappop(min_heap)  # Extract the smallest element
        merged.append(val)
        
        # Push the next element from the same array, if any
        if elem_idx + 1 < len(arrays[arr_idx]):
            heapq.heappush(min_heap, (arrays[arr_idx][elem_idx + 1], arr_idx, elem_idx + 1))
    
    return merged

def print_array(array):
    # Print the array elements as space-separated values
    print(" ".join(map(str, array)))

if __name__ == "__main__":
    # Example 1: Merging three sorted arrays
    arrays1 = [
        [1, 3, 5, 7],
        [2, 4, 6, 8],
        [0, 9, 10, 11]
    ]
    
    merged_array1 = merge_k_sorted_arrays(arrays1)
    print("Merged array (Example 1):")
    print_array(merged_array1)
    
    # Example 2: Another test case with three sorted arrays
    arrays2 = [
        [1, 3, 7],
        [2, 4, 8],
        [9, 10, 11]
    ]
    
    merged_array2 = merge_k_sorted_arrays(arrays2)
    print("Merged array (Example 2):")
    print_array(merged_array2)
