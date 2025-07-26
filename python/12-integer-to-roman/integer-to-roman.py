class Solution(object):
    def intToRoman(self, num):
        s = ""
        while(num != 0):
            if(num >= 1000):
                num = num - 1000
                s = s + "M"
            elif(num < 1000 and num >= 100):
                value = num / 100
                if(value == 9):
                    s = s + "C" + "M"
                    num = num - 900
                elif(value == 4):
                    s = s + "C" + "D"
                    num = num - 400
                elif(value >= 5):
                    s = s + "D"
                    num = num - 500
                else:
                    s = s + "C"
                    num = num - 100
            elif(num < 100 and num >= 10):
                value = num / 10
                if(value == 9):
                    s = s + "X" + "C"
                    num = num - 90
                elif(value == 4):
                    s = s + "X" + "L"
                    num = num - 40
                elif(value >= 5):
                    s = s + "L"
                    num = num - 50
                else:
                    s = s + "X"
                    num = num - 10
            else:
                value = num / 1
                if(value == 9):
                    s = s + "I" + "X"
                    num = num - 9
                elif(value == 4):
                    s = s + "I" + "V"
                    num = num - 4
                elif(value >= 5):
                    s = s + "V"
                    num = num - 5
                else:
                    s = s + "I"
                    num = num - 1
                
        return s
                
                
            
                
        