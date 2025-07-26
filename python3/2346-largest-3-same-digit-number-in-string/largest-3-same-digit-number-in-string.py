class Solution:
    def largestGoodInteger(self, num: str) -> str:

        dict_thing = {"000":0, "111":0,"222":0,"333":0,"444":0,"555":0,"666":0,"777":0,"888":0,"999":0}

        for i in range(0, len(num) - 2):
            num_thing = int(num[i:i+3])
            if num_thing % 111 != 0:
                continue
            else:
                dict_thing[num[i:i+3]] += 1
                
        
        res = ""

        for key in dict_thing:
            if dict_thing[key] != 0:
                res = key
        
        return res


        

    



    
