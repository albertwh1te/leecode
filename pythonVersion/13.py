class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numerals = {"M": 1000,
                    "D": 500,
                    "C": 100,
                    "L": 50,
                    "X": 10,
                    "V": 5,
                    "I": 1}
        sum = 0
        s = s[::-1]
        last = None
        for x in s:
            if last and numerals[x] < last:
                sum -= 2 * numerals[x]
            sum += numerals[x]
            last = numerals[x]
        return sum
