## Approach

keep a set as a window of last k elements. while looping, if current num is already in window, then duplicate distance is <= k. add current num and remove the element that goes out of window.
TC = O(n)
SC = O(min(n, k))
