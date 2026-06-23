## Approach

*   The main idea here is to reverse the whole array, and reverse first k parts nums[:k] and nums[k:n]
	
* 	then i=do k = k%n , why mean if n = 4 and k = 8 , the no rotations is unchanged

k = 2
[1, 2, 3, 4, 5]
				|
			    v
	
[5, 4, 3, 2, 1]
				|
				v
[4, 5, 3 ,2 1]
				|
				v
[4, 5, 1, 2, 3] == solution

TC = O(n)
SC = O(1)
