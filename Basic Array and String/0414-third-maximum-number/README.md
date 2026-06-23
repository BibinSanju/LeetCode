## Approach

so the idea is to keep first, second and third maximum distinct values while looping once. if the current number is already one of them i skip it, otherwise i shift the values based on where it fits. at the end if third never changed, return first.
TC = O(n)
SC = O(1)
