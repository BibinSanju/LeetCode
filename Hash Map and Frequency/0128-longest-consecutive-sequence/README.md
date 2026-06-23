## Approach

put all nums in a set for O(1) lookup. i only start counting from a number if num - 1 is not present, because that means it is the start of a sequence. then keep moving forward while next number exists.
TC = O(n)
SC = O(n)
