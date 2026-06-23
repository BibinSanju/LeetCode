## Approach

use slow and fast pointers. slow moves one step, fast moves two steps. if there is a cycle, both pointers will meet. if fast reaches null, no cycle.
TC = O(n)
SC = O(1)
