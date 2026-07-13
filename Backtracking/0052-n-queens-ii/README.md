**Problem Type**

Backtracking, return all valid solution count, place n queens safely on an n x n board.

**Idea**

Maintainthree sets where:

```
cols = columns already having a queen
diag1 = diagonals already having a queen using row - col
diag2 = diagonals already having a queen using row + col
```

**Base case:**

`row == n`
Because if we successfully placed queens in all n rows, one valid board is found.

**Recurrence**

For each row, try every column col:

```if col not in cols and row - col not in diag1 and row + col not in diag2: 
place queen     
backtrack(row + 1)     
remove queen
```

**Complexity**

TC = $$O(n!)$$
SC = $$O(n^2)$$
