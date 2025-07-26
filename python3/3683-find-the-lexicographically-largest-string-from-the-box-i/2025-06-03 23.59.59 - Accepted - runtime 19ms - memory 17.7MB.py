class Solution:
    def answerString(self, word: str, numFriends: int) -> str:

        if numFriends == 1:
            return word
        
        res = ""
        for i in range(len(word)):
            res = max(res, word[i:i+len(word)-numFriends+1])
        
        return res


        