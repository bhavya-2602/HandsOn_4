    Problem 1

    The mergeTwoArrays method, joins two sorted arrays,it runs in O(n1 + n2), where n1 and n2 be the size of each array being combined. The mergeSortedArrays method which merges K arrays of size N each involves recursively 
    splitting the arrays into halves and merging. The depth of recursion was O(log K ) and at each level of recursion we were doing O(k*k). Hence,the overall time complexity of the whole merging process is O(K * Nlog(k)) 
    where K is the number of arrays and N is
