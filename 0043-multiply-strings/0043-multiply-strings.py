class Solution(object):
    def multiply(self, num1, num2):
        num1Int = 0
        num2Int = 0

        for char in num1:
            digit = ord(char) - ord('0')
            num1Int = num1Int * 10 + digit

        for char in num2:
            digit = ord(char) - ord('0')
            num2Int = num2Int * 10 + digit

        product = num1Int * num2Int
        result = str(product)
        return result
