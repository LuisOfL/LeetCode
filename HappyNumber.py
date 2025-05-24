class Solution(object):
    def isHappy(self, n):
        def suma_cuadrados(num):
            total = 0
            while num > 0:
                digito = num % 10
                total += digito ** 2
                num //= 10
            return total

        slow = n
        fast = n

        while True:
            slow = suma_cuadrados(slow)        
            fast = suma_cuadrados(suma_cuadrados(fast))  
            if slow == 1 or fast == 1:
                return True  
            if slow == fast:
                return False
