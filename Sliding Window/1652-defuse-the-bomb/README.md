Idea:
For each index:
* If k > 0, replace it with the sum of the next k numbers.
* If k < 0, replace it with the sum of the previous abs(k) numbers.
* If k == 0, replace everything with 0.
Because the array is circular, use modulo indexing.

TC = O(n * |k|)
SC = O(1) besides output.
