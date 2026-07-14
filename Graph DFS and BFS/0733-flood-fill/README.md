**Flood FIll - BFS**

**Idea**

* start from the sr, sc
* store the color there
* initialize a deque and push the current r,c
* loop through grid, when the adjacent cell has the same color as `(sr,src)`, push it in q

**TC**

$$O(M x N)$$

**SC**

$$O(M x N)$$
