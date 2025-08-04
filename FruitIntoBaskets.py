class Solution(object):
    def totalFruit(self, fruits):
        basket = {}
        start = 0
        max_len = 0

        for end in range(len(fruits)):
            fruit = fruits[end]
            if fruit in basket:
                basket[fruit] += 1
            else:
                basket[fruit] = 1

            while len(basket) > 2:
                left_fruit = fruits[start]
                basket[left_fruit] -= 1
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                start += 1

            current_len = end - start + 1
            if current_len > max_len:
                max_len = current_len

        return max_len
