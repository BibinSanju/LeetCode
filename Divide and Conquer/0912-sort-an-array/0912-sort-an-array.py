class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left, mid, right):
            l_arr, r_arr = nums[left:mid+1], nums[mid+1:right+1]
            l,r,k = 0,0,left
            while l < len(l_arr) and r < len(r_arr):
                if l_arr[l] <= r_arr[r]:
                    nums[k] = l_arr[l]
                    l+=1
                else:
                    nums[k] = r_arr[r]
                    r+=1
                k+=1
            
            while l < len(l_arr):
                nums[k] = l_arr[l]
                l+=1
                k+=1
            
            while r < len(r_arr):
                nums[k]= r_arr[r]
                r+=1
                k+=1


        def merge_sort(left, right):
            if left < right:
                mid = (left + right) // 2
                l_arr = merge_sort(left, mid)
                r_arr = merge_sort(mid+1, right)

                merge(left, mid, right)
            return

        merge_sort(0,len(nums)-1)
        return nums
