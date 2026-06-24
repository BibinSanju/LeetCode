idea is fixed sliding window, 

* if len(s1) > len(s2): return False
* calc, counter for s1 and s1[:len(s1)]
* initally check if s1c == window

* then add right elem, remove left elem(if key == 0, del it)compare both window and s1c
* if == return true instantly

TC = O(n+m)
SC = O(1)
