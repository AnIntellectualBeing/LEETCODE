class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * (2*n)
        j = n
       # i = 0
        for i in range(n):
            ans[i*2] = nums[i]
            ans[(i *2 )+1] = nums[ n + i]

        return ans


        
