another dynamic sliding window question that follows the same pattern

* we need  window (dict)
* we keep track of highest frequency element in the window (count)
* we know [ AABA ] we would replace 1 B instead of 3 A, so we check if window size  (r-l+1) - mostFreq >k so we need more replacements than k , so we shink the window

TC = O(n)
SC = O(1)
