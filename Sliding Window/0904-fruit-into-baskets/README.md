The same **dynamic sliding window** idea, where basket(window) size is <=2 , so when r is different fruit, i shrink the left pointer till capacity of basket <=2, record max

TC = O(n)
SC = O(1) -> constant basket size = 2
