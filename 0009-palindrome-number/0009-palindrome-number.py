class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        num = x
        reverse = 0
        while num > 0:
            digit = num % 10
            reverse = reverse * 10 + digit
            num //= 10 
        return reverse == x
