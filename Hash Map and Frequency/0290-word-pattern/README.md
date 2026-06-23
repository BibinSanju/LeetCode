## Approach

split s into words. if count does not match pattern length, false. then use two maps, pattern char -> word and word -> pattern char, to make sure the relation is bijective.
TC = O(n)
SC = O(n)
