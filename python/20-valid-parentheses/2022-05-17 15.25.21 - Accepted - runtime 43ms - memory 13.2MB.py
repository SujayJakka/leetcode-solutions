class Solution(object):
       def isValid(self, s):
        stack = []
        if s[0]==")" or s[0]=="]" or s[0] == '}':
            return False
        if(len(s) <= 1):
            return False
        for i in s:
            if i=='(' or i =='{' or i=="[":
                stack.append(i)
            elif i == ')':
                if len(stack)==0 or stack.pop()!='(':
                    return False
            elif i == '}':
                if len(stack)==0 or stack.pop()!='{':
                    return False
            elif i == ']':
                if len(stack)==0 or stack.pop()!='[':
                    return False
        if(len(stack) == 0):
            return True
                    
            
        