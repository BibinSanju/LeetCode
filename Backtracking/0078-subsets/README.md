Backtracking,

* use ans [] to store subsets
* maintain a list (path) to keep track of current subsequence
* parameter ind to keep track of the current index we are in


**Base Case**:
if ind == len(nums) -> we add a copy of path in ans 

(**important note** : dont just apped path, python stores same reference variable in ans, so in future it can change so use path.copy() )

**Main recursion**:
* include current element in path, and proceed to next element
* then we exclude it from path (path.pop())
* then we proceed by skipping the element


TC = O( 2^n)
SC = O(n)
