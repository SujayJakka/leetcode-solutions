class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        res = 0
        # Only add boxes that can be opened
        queue = Deque()
        keys_found = [0] * len(candies)
        boxes_found = [0] * len(candies)

        for box in initialBoxes:
            boxes_found[box] = 1
            if status[box] == 1:
                queue.append(box)
                res += candies[box]

        while queue:
            box = queue.popleft()

            # If we find a key to an already seen box, append the box onto the queue if it has not been opened
            for key in keys[box]:
                keys_found[key] = 1
                if boxes_found[key] == 1 and status[key] == 0:
                    queue.append(key)
                    status[key] = 1
                    res += candies[key]

            # Append the new boxes to the queue if key is found or if box is already open
            for new_box in containedBoxes[box]:
                boxes_found[new_box] = 1
                if keys_found[new_box] or status[new_box] == 1:
                    queue.append(new_box)
                    status[new_box] = 1
                    res += candies[new_box]
        
        return res
        