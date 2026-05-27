#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        copy = n
        digits = len(str(n))
        sum = 0
        while(n>0):
            last_dig = n%10
            sum = sum + (last_dig**digits)
            n = n//10
        if sum == copy:
            return True
        else:
            return False