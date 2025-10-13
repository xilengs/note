# 元音拼写检查器
from multiprocessing.connection import answer_challenge

class Solution:
    def spellchecker(self, wordlist, queries):
        origin = set(wordlist)
        lower_to_origin = {}
        vowel_to_origin = {}
        trans = str.maketrans("aeiou", "?????")  # 替换元音为 '?'

        for s in reversed(wordlist):
            lower = s.lower()
            lower_to_origin[lower] = s  # 例如 kite -> KiTe
            vowel_to_origin[lower.translate(trans)] = s  # 例如 k?t? -> KiTe

        for i, q in enumerate(queries):
            if q in origin:  # 完全匹配
                continue
            lower = q.lower()
            if lower in lower_to_origin:  # 不区分大小写的匹配
                queries[i] = lower_to_origin[lower]
            else:  # 不区分大小写+元音模糊匹配
                queries[i] = vowel_to_origin.get(lower.translate(trans), "")
        return queries
