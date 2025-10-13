# 找到频率最高的元音和辅音
class Solution:
    def maxFreqSum(self, s: str) -> int:
        alphabet = {}
        vowel_max = ['', 0]
        consonant_max = ['', 0]
        for letter in s:
            if letter in alphabet:
                alphabet[letter] += 1
            else:
                alphabet[letter] = 1

        for key, value in alphabet.items():
            if key in 'aeiou' and value > vowel_max[1]:
                vowel_max = [key, value]
            elif key not in 'aeiou' and value > consonant_max[1]:
                consonant_max = [key, value]

        return vowel_max[1] + consonant_max[1]
