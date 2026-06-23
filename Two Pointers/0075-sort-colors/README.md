## Approach

the idea is we know array has 0,1,2. we keep track of 3 pointer , one for array traversal (i) , one for left  side swap (0 will be swapped to left) and right for 2 (2 will be swapped to right) so at the end all 0's move to left and all 2's to right . so automatically 1's come in centre

TC = O(n)
SC = O(1)
