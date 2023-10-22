class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        minToLeft = [float("inf")] * n
        minToRight = [float("inf")] * n

        curMin = float("inf")
        for i in range(n):
            if curMin < nums[i]:
                minToLeft[i] = curMin
            curMin = min(curMin, nums[i])

        curMin = float("inf")
        for i in range(n - 1, -1, -1):
            if nums[i] > curMin:
                minToRight[i] = curMin
            curMin = min(curMin, nums[i])

        ans = float("inf")
        for i in range(n):
            if minToLeft[i] != float("inf") and minToRight[i] != float("inf"):
                ans = min(ans, minToLeft[i] + nums[i] + minToRight[i])

        if ans == float("inf"):
            return -1
        return ans