class Solution:
    def isValid(self, s: str) -> bool:
        d={ ")":"(", "]":"[", "}":"{" }
        stack=[]
        for symbol in s :
            if symbol in d.keys() and stack:
                if d[symbol]==stack[-1]:
                    stack.pop()
                else:
                    stack.append(symbol)
            else:
                stack.append(symbol)

        if len(stack)>=1:
            return False
        else:
            return True