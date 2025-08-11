class Solution:
    def reorderedPowerOf2(self, n):
        
        def signature(num):
            return ''.join(sorted(str(num)))
        
        target_sig = signature(n)
    
        for i in range(31):  
            if signature(1 << i) == target_sig:
                return True
        return False
