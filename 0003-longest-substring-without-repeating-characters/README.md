so, here i need a subarray with unique elements, i maintain a variable sliding window, where i iterate my right pointer , while my left pointer stays at the window start. so if i encounter an element in right where it is already inside the window , i just jump to the dup element inside that window (subarray is contigious) , i maintain window elems in set for o(1) lookups, while jumping , i remove the elemtents is jumped over from the set 

TC = o(n)
sc= o(n) or o(26)
