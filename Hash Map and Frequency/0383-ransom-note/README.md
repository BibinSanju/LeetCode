## Approach

count all letters in magazine first. then for every char in ransomNote, use one count. if a char is missing or count becomes 0 before using it, return false.
TC = O(n + m)
SC = O(k)
