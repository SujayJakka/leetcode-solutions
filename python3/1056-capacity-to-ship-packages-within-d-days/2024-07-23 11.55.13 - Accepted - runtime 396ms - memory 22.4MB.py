class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        res = sum(weights)

        def is_enough(capacity, days):
            curr_days = 0
            curr_sum = 0

            for weight in weights:
                if curr_sum + weight > capacity:
                    curr_days += 1
                    curr_sum = weight
                else:
                    curr_sum += weight
            
            curr_days += 1
            return True if curr_days <= days else False
        

        l, r = max(weights), sum(weights)

        while l <= r:
            mid = (l + r) // 2

            if is_enough(mid, days):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res

        