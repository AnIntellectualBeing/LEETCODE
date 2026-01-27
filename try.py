class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num = 1
        if nums[-1] == nums[-2] and len(nums) > 2:
            return list([nums[-1],nums[-1]-1])
        if (nums[0]>nums[0]):
            
            last = nums[-1]

            for i in nums[::-1]:
                if(i != num):
                    l = [nums[num+1],num]
                    return l
                num +=1
        else:
                
            for i in nums:
                if(i != num):
                    l = [nums[num-1],num]
                    return l
                num +=1
