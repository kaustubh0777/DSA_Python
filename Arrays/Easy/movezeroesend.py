class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        r=0
        w=0
        n=len(nums)

        while(r<n):
            if nums[r]==0:
                r+=1
            else:
                nums[r],nums[w]=nums[w],nums[r]
                w+=1
                r+=1
        

        