class Solution(object):
    def isPalindrome(self, x):
        if(x < 0):
            return False
        else:
            x = str(x)
            rev = x[::-1]
            if( x == rev):
                return True 
            else:
                return False
