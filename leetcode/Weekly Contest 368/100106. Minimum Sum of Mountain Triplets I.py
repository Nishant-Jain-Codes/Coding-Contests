class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        ans = 1e7
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if(nums[i]<nums[j] and nums[j]>nums[k]):
                        ans = min(ans,nums[i]+nums[j]+nums[k])
        if ans == 1e7:
            ans = -1
        return ans
        