class Solution:
    def sortVowels(self, s):
        vowel = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        tmp = []
        t = ""
        for i in range(len(s)):
            if s[i] in vowel:
                tmp.append(s[i])
        tmp.sort()
        a = 0
        for letter in s:
            if letter in vowel:
                t = t + tmp[a]
                a += 1
            else:
                t = t + letter

        return t
    
def test():
    s = Solution()
    print(s.sortVowels("lEetcOde"))
    print(s.sortVowels("lYmpH"))

test()
        