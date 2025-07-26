class Solution(object):
    def threeSum(self, nums):
        result = []
        if(len(nums) == 0):
            return result
        if(len(nums) == 1 and [0] == 0):
            return result
        nums.sort()
        for i in range (0, len(nums)-2):
            p = i + 1
            q = len(nums) - 1
            while(p < q):
                poss = nums[i] + nums[p] + nums[q]
                if(poss > 0):
                    q-=1
                elif(poss < 0):
                    p+=1
                else:
                    row = []
                    row.append(nums[i])
                    row.append(nums[p])
                    row.append(nums[q])
                    result.append(row)
                    q-=1
                    p+=1
        newresult = []
        for x in result:
            if(x not in newresult):
                newresult.append(x)
        return newresult
                
            
        
        
        
        