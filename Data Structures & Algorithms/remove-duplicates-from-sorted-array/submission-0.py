class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = l+1
        while r <= len(nums)-1 :
            if nums[l] == nums[r]:
                nums.pop(r)
                
            else:
                l+=1
                r+=1
            n = len(nums)-1
        return l+1



        