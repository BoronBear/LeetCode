import re

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(' ')
        multiplier = 1
        if len(s) == 0:
            return 0
        if (s[0] == '+') or (s[0] == '-'):
            multiplier = 2 * (s[0] == '+') - 1
            s = s[1:]
        search_str = re.search(r'^\d+', s)
        if search_str == None:
            return 0
        parsed_int = int(search_str.group())
        if (multiplier == 1) and (parsed_int > 2**31 - 1):
            parsed_int = 2**31 - 1
        elif (multiplier == -1) and (parsed_int > 2**31):
            parsed_int = 2**31
        return multiplier * parsed_int