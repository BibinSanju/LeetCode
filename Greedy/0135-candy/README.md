it resembels the two pointer pattern with two passes (done in cookies , greed sum), left to right pass to fill asc and right to left to fil desc

initialised ans = [1,1..1] because every child should get a candy

pass 1 : 
				1->n, if i > i-1 we need extra candy, so ans[i-1] +1

pass 2:
						n-2->0 if i > i+1 we need extra candy, but before assiging we check if
						it was already satisfied in 1st pass by max(ans[i], ans[i+1]+1)
						

TC = O(n)
SC = O(n) -> suggested = O(1) -> by single pass method
