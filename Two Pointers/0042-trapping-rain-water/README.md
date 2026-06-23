## Approach

use left and right pointers with left max and right max. always move the side with smaller height, because water on that side depends on its max boundary. add trapped water when current height is below max.
TC = O(n)
SC = O(1)
