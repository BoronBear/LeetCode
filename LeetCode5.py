class Solution:
    def longestPalindrome(self, s: str) -> str:
        return_palindrome = s[0]
        for i in range(len(s)):
            start_ind, end_ind = i, i
            while (start_ind > 0) and (end_ind < len(s) - 1):
                if s[start_ind - 1] == s[end_ind + 1]:
                    start_ind -= 1
                    end_ind += 1
                else:
                    break
            if end_ind - start_ind + 1 > len(return_palindrome):
                return_palindrome = s[start_ind: end_ind + 1]
        for i in range(len(s) - 1):
            start_ind, end_ind = i, i + 1
            if s[start_ind] == s[end_ind]:
                while (start_ind > 0) and (end_ind < len(s) - 1):
                    if s[start_ind - 1] == s[end_ind + 1]:
                        start_ind -= 1
                        end_ind += 1
                    else:
                        break
                if end_ind - start_ind + 1 > len(return_palindrome):
                    return_palindrome = s[start_ind: end_ind + 1]

        return return_palindrome