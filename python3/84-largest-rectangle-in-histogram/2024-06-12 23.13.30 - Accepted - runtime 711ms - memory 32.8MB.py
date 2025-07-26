class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        ptr = 0
        max_area = 0
        stack = []

        while ptr < len(heights):

            index = ptr
            height = heights[ptr]

            while stack and stack[-1][0] > height:
                max_area = max(stack[-1][0] * (ptr - stack[-1][1]), max_area)
                index = min(index, stack[-1][1])
                stack.pop()
            
            stack.append((height, index))

            ptr += 1
        
        for height, index in stack:
            max_area = max(height * (len(heights) - index), max_area)

        return max_area
        