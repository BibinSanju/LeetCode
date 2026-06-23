## Approach

sort people first. then try to pair the lightest person with the heaviest person. if they fit, move both pointers, otherwise the heaviest goes alone. every step uses one boat.
TC = O(n log n)
SC = O(1) extra
