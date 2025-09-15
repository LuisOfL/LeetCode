class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        l = text.split()
        cont = len(l)
        for x in l:
            for y in x:
                if y in brokenLetters:
                    cont -= 1
                    break
        return cont
