## Approach

move fast pointer n steps ahead. then move slow and fast together until fast reaches the end. now slow is just before the node to remove, so skip that node. if fast became null after first move, remove head.
TC = O(n)
SC = O(1)
