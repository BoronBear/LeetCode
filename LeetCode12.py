class Solution:
    def intToRoman(self, num: int) -> str:
        return_string = ''
        temp = num
        for i in range(num // 1000):
            return_string += 'M'
        temp = temp % 1000

        if temp >= 900:
            temp -= 900
            return_string += 'CM'
        if temp >= 500:
            temp -= 500
            return_string += 'D'
        if temp >= 400:
            temp -= 400
            return_string += 'CD'
        else:
            for i in range(temp // 100):
                return_string += 'C'
            temp = temp % 100

        if temp >= 90:
            temp -= 90
            return_string += 'XC'
        if temp >= 50:
            temp -= 50
            return_string += 'L'
        if temp >= 40:
            temp -= 40
            return_string += 'XL'
        else:
            for i in range(temp // 10):
                return_string += 'X'
            temp = temp % 10

        if temp >= 9:
            temp -= 9
            return_string += 'IX'
        if temp >= 5:
            temp -= 5
            return_string += 'V'
        if temp >= 4:
            temp -= 4
            return_string += 'IV'
        else:
            for i in range(temp):
                return_string += 'I'
        return return_string

