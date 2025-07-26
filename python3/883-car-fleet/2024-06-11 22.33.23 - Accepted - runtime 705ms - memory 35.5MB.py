class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        combined_list = []
        for i in range(len(position)):
            combined_list.append([position[i], speed[i]])
        
        combined_list.sort(key=lambda x: x[0])

        stack = []

        for i in range(len(combined_list) - 1, -1, -1):

            stack.append(combined_list[i])

            if len(stack) > 1:
                time_point_1 = (target - combined_list[i][0]) / combined_list[i][1]
                time_point_2 = (target - stack[-2][0]) / stack[-2][1]

                if time_point_1 <= time_point_2:
                    stack.pop()

        return len(stack)
