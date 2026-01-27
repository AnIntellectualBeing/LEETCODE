class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_i = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            if count > max_i:
                max_i = count
            if nums[i] == 0:
                count = 0
        return max_i
