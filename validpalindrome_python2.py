class Solution:

    def isPalindrome(self, s: str) -> bool:
        
        if s == " ":
            return True
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left +=1

            while right > left and not s[right].isalnum():
                right -=1
            
            if   s[left] != s[right]:
                return False

            
            left +=1
            right -=1
            
        return True
        
    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s):
            return True
        temp = ""
        for i in range(len(s)):
            temp =  s[:i] + s[i+1:]
            if self.isPalindrome(temp):
                 return True
        return False

