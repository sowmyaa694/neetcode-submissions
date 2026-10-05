class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        must={"}":"{","]":"[",")":"("}
        for i in s:
            if i in "{[(":
                stack.append(i)
            if i in must:
                if stack and stack[-1]==must[i]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False

            

        