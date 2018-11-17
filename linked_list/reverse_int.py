class Solution:
# 123
# 321

    def __init__(self, input):
        self.input = input
    def reverse_int(self):
        answer = 0
        sign = 1 if self.input>0 else -1
        self.input = abs(self.input)

        while self.input > 0 :
            answer = answer * 10 + self.input % 10
            self.input = self.input // 10 # should be '//' instead of '/' for computing reminder

        return answer * sign
    
print(Solution(123).reverse_int())
        
        




