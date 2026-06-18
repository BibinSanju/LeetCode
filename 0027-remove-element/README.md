the idea here is to use a pointer to find the next elem to remove,

[2, 3, 3, 2] ; v = 3

i = 0, j = 0

 will copy everything nums[j] to nums[i] where j pointer skips the removable elem, so removable elem gets overwritten, i will always increment by one as a array index tracker, we skip removable element and overwrite it
