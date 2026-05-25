1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        if x < 0:
4            return False
5        else:
6            rev = 0
7            copy = x
8
9            while x != 0:
10                last = x % 10
11                rev = rev * 10 + last
12                x = x//10
13            if copy == rev:
14                return True
15            else:
16                return False
17        