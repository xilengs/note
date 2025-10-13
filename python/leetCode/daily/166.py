# 分数到小数

class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator % denominator == 0:
            return str(numerator // denominator)


        answer = ""
        if (numerator < 0) != (denominator < 0):
            answer += "-"
            numerator, denominator = abs(numerator), abs(denominator)
        answer += str(numerator // denominator) + "."
        remained = numerator % denominator

        remainder_seen = {}
        index = 0
        decimal_part = ""

        while remained != 0:
            if remained in remainder_seen:
                start_index = remainder_seen[remained]
                not_repeating = decimal_part[:start_index]
                repeating = decimal_part[start_index:]
                return answer + not_repeating + "(" + repeating + ")"
            remainder_seen[remained] = index
            remained *= 10
            decimal_part += str(remained // denominator)
            remained = remained % denominator
            index += 1

        return answer + decimal_part
