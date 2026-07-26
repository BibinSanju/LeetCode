# Intuition
Since allowed movement directions depend on whether the current action is **odd-numbered** (Action 1, 3, 5...) or **even-numbered** (Action 2, 4, 6...), the state at any point in the grid can be defined by three parameters: `(row, col, is_odd_action)`.

Since edge weights (movement/waiting costs) are non-negative, we can find the minimum cost to reach the target cell `(m - 1, n - 1)` using **Dijkstra's Algorithm**.

# Approach
1. **State Definition**:
   - `dist[r][c][is_odd]` stores the minimum cost to reach cell `(r, c)` where `is_odd` is `True` (or `1`) if the next action is odd-numbered, and `False` (or `0`) if it is even-numbered.
   - Initial state: `(0, 0, is_odd = True)` with initial entrance cost `(0 + 1) * (0 + 1) = 1`.

2. **Actions & Parity Rules**:
   Taking any action (moving or waiting) flips the parity (`next_is_odd = not is_odd`):
   - **Wait**: Cost added is `penalty[r][c]`.
   - **Move to `(nr, nc)`**: Entrance cost added is `(nr + 1) * (nc + 1)`.
     - **ODD action** expects `RIGHT` or `DOWN`. Moving `LEFT` or `UP` violates the rule.
     - **EVEN action** expects `LEFT` or `UP`. Moving `RIGHT` or `DOWN` violates the rule.
     - If the rule is violated, add extra penalty `penalty[r][c]` from the source cell.

3. **Shortest Path**:
   - Use a Priority Queue (Min-Heap) to process states in increasing order of cumulative cost. The first time cell `(m - 1, n - 1)` is popped from the queue, we return its cost.

# Complexity
- Time complexity:
$$O(m \cdot n \log(m \cdot n))$$

- Space complexity:
$$O(m \cdot n$$
