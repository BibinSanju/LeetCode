normal binary search,

* given array is sorted so we iteratively find mid of array, and check check whether its the target, is yes, return mid
* or is t>m then its in right side of mid so, left = mid+1
* else it in left side so, right = mid-1
* if not found return -1
