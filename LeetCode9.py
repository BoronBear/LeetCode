class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        for i in range( (len(strx) + 1) // 2):
            if strx[i] != strx[len(strx) - 1 - i]:
                return False
        return True