class Solution(object):
    def romanToInt(self, s):
        answer = 0
        s = s[::-1]
        s = s + "O"
        i = 0
        while(i < len(s)-1):
                if(s[i] == "I"):
                    answer = answer + 1
                elif(s[i] == "V"):
                    if(s[i+1] == "I"):
                        answer = answer + 4
                        i+=1
                    else:
                        answer = answer + 5
                elif(s[i] == "X"):
                    if(s[i+1] == "I"):
                        answer = answer + 9
                        i+=1
                    else:
                        answer = answer + 10
                elif(s[i] == "L"):
                    if(s[i+1] == "X"):
                        answer = answer + 40
                        i+=1
                    else:
                        answer = answer + 50
                elif(s[i] == "C"):
                    if(s[i+1] == "X"):
                        answer = answer + 90
                        i+=1
                    else:
                        answer = answer + 100
                elif(s[i] == "D"):
                    if(s[i+1] == "C"):
                        answer = answer + 400
                        i+=1
                    else:
                        answer = answer + 500
                elif(s[i] == "M"):
                    if(s[i+1] == "C"):
                        answer = answer + 900
                        i+=1
                    else:
                        answer = answer + 1000
                i+=1
        return answer
        