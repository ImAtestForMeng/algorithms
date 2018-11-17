from array_stack import Stack

class Solution:
    def __init__(self):
        self.stack = Stack()
    
    def check_paranthese(self, input_str):
        balanced = True
        index = 0

        while index < len(input_str) and balanced:
            symbol = input_str[index]
            # for open parenthssis
            if symbol in "[{(":
                self.stack.push(symbol)
            # for close parenthesis
            if symbol in "]})":
                close_paren = self.stack.pop()
                balanced = self.compare(symbol, close_paren)
            else:
                if self.stack.isEmpty():
                    balanced = False
            index = index + 1   

        if balanced and self.stack.isEmpty():
            print("Pass")
            return 
        else:
            print("Fail")
            return

    def compare(self, open_paran, close_paran):
        if open_paran == "{" and close_paran == "}":
            return True
        if open_paran == "[" and close_paran == "]":
            return True
        if open_paran == "(" and close_paran == ")":
            return True
        else:
            return False


input_str = "([])"
Solution().check_paranthese(input_str)