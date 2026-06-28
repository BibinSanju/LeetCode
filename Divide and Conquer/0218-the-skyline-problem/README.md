Each building is [left, right, height].

Base case: one building gives:
[(left, height), (right, 0)]

* Divide buildings into two halves.
* Recursively get skyline for left half and right half.
* Merge both skylines:Track current height from left skyline: h1
* Track current height from right skyline: h2
* Visible height is max(h1, h2)

Add a point only when visible height changes.

**key idea**:
Skyline height at any x = max(current left height, current right height)
Avoid duplicate consecutive heights.

TC = O( n log n )
SC = O( n )
