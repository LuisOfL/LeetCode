class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        dic_s = {}
        dic_t = {}

        for letra in s:
            dic_s[letra] = dic_s.get(letra, 0) + 1

        for letra in t:
            dic_t[letra] = dic_t.get(letra, 0) + 1

        return dic_s == dic_t
