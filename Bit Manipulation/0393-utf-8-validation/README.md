As per UTF-8 rules

* use mask 128 (10000000) to count 1
* if count == 0, valid 1byte
* count == 1 or >4 , invalid
* else check for continuation 0b10 (10xxx)

TC = O(n)
SC = O(1)
