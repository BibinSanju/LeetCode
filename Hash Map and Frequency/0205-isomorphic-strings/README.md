## Approach

i maintain two maps, s -> t and t -> s. while looping both strings together, if an old mapping does not match the current char, return false. this keeps the mapping one-to-one.
TC = O(n)
SC = O(k)
