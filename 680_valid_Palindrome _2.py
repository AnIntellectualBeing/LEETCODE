class Solution:
    
    def validPalindrome(self, s: str) -> bool:
        s = s.lower()
        right = len(s)-1

        left = 0
        
        
        
        while left < right:
            
            if s[right] != s[left]:
                l1 , r1 = left , right-1
                isValid = True
                while l1 < r1:
                    if s[r1] != s[l1]:
                        isValid = False
                        break
                    l1 +=1
                    r1 -=1

                isValid2 = True
                l2 , r2 = left+1 , right
                while l2 < r2:
                    if s[r2] != s[l2]:
                        isValid2 = False
                        break
                    l2 +=1
                    r2 -=1
                return isValid or isValid2
            right -=1
            left +=1
        return True
