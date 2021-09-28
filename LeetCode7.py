class Solution:
    def reverse(self, x: int) -> int:
        lim_nums = [str(2**31 - 1), str(2**31)]
        mode = 0
        if x < 0:
            mode = 1

        strx = str(x * (1 - mode * 2))
        if len(strx) > len(lim_nums[mode]):
            return 0

        elif len(strx) == len(lim_nums[mode]):
            for i in range(len(strx)):
                if int(strx[len(strx) - i - 1]) > int(lim_nums[mode][i]):
                    return 0
                elif int(strx[len(strx) - i - 1]) < int(lim_nums[mode][i]):
                    break

        return (1 - mode * 2) * int(strx[::-1])
