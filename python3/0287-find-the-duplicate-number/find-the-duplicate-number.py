class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hare, turtle = 0, 0

        while True:
            hare = nums[hare]

            turtle = nums[nums[turtle]]

            if hare == turtle:
                break

        hare = 0
        
        while True:
            hare = nums[hare]
            turtle = nums[turtle]

            if hare == turtle:
                return turtle

        
        



    