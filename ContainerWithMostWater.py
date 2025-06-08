class Solution(object):
    def maxArea(self, height):
        izquierdo   = 0
        derecho = len(height)-1
        AreaM = 0
        AreaT = 0
        Base = 0
        Altura = 0
        while derecho >= izquierdo:
            Base = derecho - izquierdo
            if  height[derecho] > height[izquierdo]:
                Altura = height[izquierdo]
            else:
                Altura = height[derecho]
            AreaT = Base * Altura
            if AreaT > AreaM:
                AreaM = AreaT
            if height[izquierdo] < height[derecho]:
                izquierdo += 1
            else:
                derecho -= 1
        return AreaM
