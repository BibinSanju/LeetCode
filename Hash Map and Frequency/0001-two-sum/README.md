## Approach

i store visited numbers in a hashmap with their index. for every num, i check if target - num is already present. if yes, that old index and current index is the answer, otherwise store current num.
TC = O(n)
SC = O(n)
