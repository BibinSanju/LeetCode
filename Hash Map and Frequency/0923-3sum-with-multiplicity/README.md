## Approach

count frequency of every value first. then try pairs of values with replacement and calculate the needed third value. depending on whether values are same or different, use combination formula from counts.
TC = O(n + u^2), u = unique values
SC = O(u)
