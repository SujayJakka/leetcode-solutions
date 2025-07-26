class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        array_1 = [0] * 26

        for char in s:
            array_1[ord(char) - 97] += 1
        for char in t:
            array_1[ord(char) - 97] -= 1
        

        for num in array_1:
            if num != 0:
                return False

        return True