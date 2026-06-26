idea is, fixed size sliding window, where i keep track of a current var_count and max, if incoming r in vow, c+=1, if outgoing l is vow, c-=1

l             r         res
vow - vow    =  0
nvow - vow  =  1
vow - nvow  = -1
