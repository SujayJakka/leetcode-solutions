class Solution:
    def isValid(self, s: str) -> bool:
        stackThing = []

        for i in range(len(s)):
            if len(stackThing) == 0:
                stackThing.append(s[i])
            else:
                if stackThing[len(stackThing) - 1] == "(":
                    if s[i] == ")":
                        stackThing.pop()
                        continue
                    else:
                        stackThing.append(s[i])
                        continue
                if stackThing[len(stackThing) - 1] == "{":
                    if s[i] == "}":
                        stackThing.pop()
                        continue
                    else:
                        stackThing.append(s[i])
                        continue
                
                if stackThing[len(stackThing) - 1] == "[":
                    if s[i] == "]":
                        stackThing.pop()
                        continue
                    else:
                        stackThing.append(s[i])
                        continue

        if len(stackThing) != 0:
            return False
        else:
            return True
