1class Solution:
2    def reverse(self, x: int) -> int:
3
4        sign = -1 if x < 0 else 1
5        x = abs(x)
6
7        rev = 0
8
9        while x != 0:
10            last_dig = x % 10
11            rev = rev * 10 + last_dig
12            x = x // 10
13
14        rev = sign * rev
15
16        if rev < -2**31 or rev > 2**31 - 1:
17            return 0
18
19        return rev