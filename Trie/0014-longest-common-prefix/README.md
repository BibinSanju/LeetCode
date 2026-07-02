So, sort the strs , it will be ordered lexographically, then we take first and last string in strs, traverse both string from 0->min(len(first,last)),

* if not same letter, then break , else add it in ans

Current complexity: O(S+M logN)
Suggested complexity: O(S)
Suggestions:
Skip sorting to achieve linear time; compare characters directly across all strings.
