class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        s = s.replace(" ", "")

        l = 0
        r = len(s) - 1

        while l < r:
            if ((ord(s[l]) > 96 and ord(s[l]) < 123) or (ord(s[l]) > 47 and ord(s[l]) < 58)) and ((ord(s[r]) > 96 and ord(s[r]) < 123) or (ord(s[r]) > 47 and ord(s[r]) < 58)):
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1
            else:
                if not ((ord(s[l]) > 96 and ord(s[l]) < 123) or (ord(s[l]) > 47 and ord(s[l]) < 58)):
                    l += 1
                if not ((ord(s[r]) > 96 and ord(s[r]) < 123) or (ord(s[r]) > 47 and ord(s[r]) < 58)):
                    r -= 1
        return True
