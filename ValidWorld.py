class Solution(object):
    def isValid(self, word):
        vowels = set('aeiouAEIOU')
        c1 = False
        c2 = False

        if len(word) < 3:
            return False

        for c in word:
            if not c.isalnum():  
                return False
            if c.isalpha():
                if c in vowels:
                    c1 = True
                else:
                    c2 = True

        return c1 and c2
