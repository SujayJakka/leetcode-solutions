class Solution(object):
    def removeDuplicates(self, nums):
        listLen = len(nums)
        if listLen <= 1:
            return listLen
        listIndex = 1
        for i in range(listIndex, listLen):
            if nums[i] != nums[i-1]:
                nums[listIndex] = nums[i]
                listIndex += 1
        return listIndex
