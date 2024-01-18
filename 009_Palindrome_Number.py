class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == x[::-1]:
            return True
        else:
            return False