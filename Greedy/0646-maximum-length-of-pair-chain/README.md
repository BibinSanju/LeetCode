another overlapping porblem,

* sort intervals by end time
* maintain var e to store previous end of chain
* if upcoming start > end , them chain grows (ie. ans+=1)

TC = O(n logn)
SC = O(logn) -> for sorting
