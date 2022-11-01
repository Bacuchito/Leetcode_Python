class Solution:
    def reverse(self, x: int) -> int:
        i = x
        newNum = 0
        
        while x > 0:
            newNum = newNum * 10 + x%10
            x = x//10
        return newNum