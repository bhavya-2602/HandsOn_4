  **Problem 1**
    
   **Prove the time complexity of the Algorithm**
    
    The mergeTwoArrays method, joins two sorted arrays,it runs in O(n1 + n2), where n1 and n2 be the size of each 
    array being combined. The mergeSortedArrays method which merges K arrays of size N each involves recursively 
    splitting the arrays into halves and merging. The depth of recursion was O(log K ) and at each level of recursion 
    we were doing O(k*k). Hence,the overall time complexity of the whole merging process is O(K * Nlog(k)) 
    where K is the number of arrays and N is is the size of each array.


   **Comment on way's you could improve your implementation**

    Thecurrent code can be improved by changing it to an iterative solution. In the case we have an large number
    of arrays or we call this function several levels deep, we can end up in recursive calls that will be too long
    and the call stack will overflow. An alternative for this issue is to perform the operation iteratively (pair-wise 
    merge of two arrays in monotone), give me this passage into simpler words.
