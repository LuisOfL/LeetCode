class Solution(object):
    def countGoodNumbers(self, n):
        MOD = 10**9 + 7
        pares = (n + 1) // 2 
        impares = n // 2      
        return (pow(5, pares, MOD) * pow(4, impares, MOD)) % MOD
