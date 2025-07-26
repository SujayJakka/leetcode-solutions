class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        stack = []
        arr = sorted(arr)
        for i in range(len(arr) - 1):
            val = arr[i + 1] - arr[i]
            while stack and val < stack[-1][1] - stack[-1][0]:
                stack.pop()

            if not stack or val == stack[-1][1] - stack[-1][0]:
                stack.append([arr[i], arr[i + 1]])

        return stack