## Approach

for every word, sort its characters and use that sorted string as key. all anagrams will get the same key, so i append them into the same list in hashmap.
TC = O(n * k log k)
SC = O(n * k)
