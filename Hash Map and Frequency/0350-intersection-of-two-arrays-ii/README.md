## Approach

count frequency of the smaller array. then loop through the other array, and if the count is still positive, add it to answer and reduce the count.
TC = O(n + m)
SC = O(min(n, m))
