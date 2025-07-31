class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        nums = sorted(nums)

        def find_num_pairs(threshold):
            
            i = 0
            count = 0
            while i < len(nums) - 1:

                if nums[i+1] - nums[i] <= threshold:
                    count += 1
                    i += 1

                i += 1

            return count

        
        # Binary search
        l, r = 0, nums[-1] - nums[0]

        while l < r:
            mid = (l + r) // 2

            if find_num_pairs(mid) >= p:
                r = mid
            else:
                l = mid + 1

        return l