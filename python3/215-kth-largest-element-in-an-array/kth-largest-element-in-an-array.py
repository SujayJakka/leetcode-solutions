class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def quick_select(arr, k):
            left, mid, right = [], [], []
            pivot = random.choice(arr)

            for num in arr:
                if pivot < num:
                    left.append(num)
                elif pivot > num:
                    right.append(num)
                else:
                    mid.append(num)
            
            if len(left) >= k:
                return quick_select(left, k)
            
            if len(left) + len(mid) < k:
                return quick_select(right, k - (len(left) + len(mid)))
            
            return pivot
        
        return quick_select(nums, k)

        