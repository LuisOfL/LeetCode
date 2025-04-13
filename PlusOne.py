class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        if digits[n-1] != 9:
            digits[n-1] += 1
        elif digits[n-1] == 9:
            if n == 1:
                digits[0] = 1
                digits.append(0)

            else:
                for i in range(n-1,-1,-1):
                    if i == n-1:
                        if digits[i] == 9:
                            digits[i] = 0
                            digits[i-1] += 1
                    if digits[i] == 10 and i != 0:
                        digits[i] = 0
                        digits[i-1] += 1
                    elif digits[i] == 10 and i == 0:
                        digits[i] = 1
                        digits.append(0)

        return digits   
