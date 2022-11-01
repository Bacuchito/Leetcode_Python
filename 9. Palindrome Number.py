class Solution:
    def isPalindrome(self, x: int) -> bool:
        # lo convertismo a string y le decimos si la inversa de el string es igual al string
        return str(x) == str(x)[::-1]

    # si no queremos convertilo a string, hacemos lo siguiente

    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False

        i = x
        newNum = 0
        while x > 0:
            newNum = newNum *10 + x%10
            x = x//10
            return newNum

    def isPalindrome2(self, x: int) -> bool:
        # lo primero que hacemos x > 0:
        if x > 0:
            i = int(str(x)[::-1])
        else:
            i = int(str(x * -1)[::-1]) * -1
        
        mi = 2 ** 31 * (-1)
        ma = 2 ** 31 - 1
        
        if i > ma or i < mi:
            return 0
        return i
      
