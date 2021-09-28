class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        row_strings = ['' for i in range((numRows - 1) * 2)]
        for i in range(len(s)):
            mod_index = i % ((numRows - 1) * 2)
            if mod_index <= numRows - 1:
                row_strings[mod_index] += s[i]
            else:
                row_strings[(numRows - 1) * 2 - mod_index] += s[i]
        return ''.join(row_strings)