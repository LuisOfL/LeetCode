class Solution(object):
    def minWindow(self, s, t):
        if not t or len(t) > len(s):
            return ''

        frec = {}
        curr_frec = {}
        for c in t:
            frec[c] = frec.get(c,0) + 1

        p1 = 0
        have = 0
        tot = len(frec)
        res = [-1,-1]
        min_len = float('inf')

        for p2 in range(len(s)):
            c = s[p2]
            curr_frec[c] = curr_frec.get(c,0) + 1

            if c in frec and curr_frec[c] == frec[c]:
                have += 1

            while have == tot:
                if (p2 - p1 + 1) < min_len:
                    min_len = p2 - p1 + 1
                    res = [p1,p2]

                left_char = s[p1]
                curr_frec[left_char] -= 1
                if left_char in frec and curr_frec[left_char] < frec[left_char]:
                    have -= 1
                p1 += 1

        if res[0] == -1:
            return ""
        return s[res[0]:res[1]+1]
