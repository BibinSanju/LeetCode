## Approach

i use a set to store what i already saw in each row, column and 3x3 box. for each filled cell, i make three keys. if any key already exists, sudoku is invalid.
TC = O(1), board is fixed 9x9
SC = O(1)
