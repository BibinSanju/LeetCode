## Approach

The idea here is to pass from left -> right and will every elem distance with the previously occured c, the we pass fro right - > left and update
min(ans[left->right] , prev - i (right-left pass))

e 1 2 3 e
|
v
e 1 2 2 1 e

TC = O(n)
SC = O(n)
