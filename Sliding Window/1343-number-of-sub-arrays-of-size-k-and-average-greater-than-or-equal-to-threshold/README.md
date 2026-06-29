idea is fixed sliding window,
* instead of calculating sum/k >= thresh every time, just multiply k * thresh and check if sum(window) >= thresh

TC = O(n)
SC = O(1)
