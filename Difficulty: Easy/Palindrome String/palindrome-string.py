class Solution:
    def isPalindrome(self, s):
        # code here
        def pal(i):
            if(i>=len(s)/2):
                return True
            if(s[i]!=s[len(s)-i-1]):
                return False
            return pal(i+1)
        return pal(0)
