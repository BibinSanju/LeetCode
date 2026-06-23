## Approach

use two pointers p1 and p2. when p1 ends, send it to headB, and when p2 ends, send it to headA. this makes both pointers travel same total length, so they meet at intersection or null.
TC = O(a + b)
SC = O(1)
