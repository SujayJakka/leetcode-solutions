
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        visited = set()
        queue = deque()

        for deadend in deadends:
            visited.add(deadend)
        
        queue.append("0000")
        if "0000" in visited:
            return -1
            
        level = 0

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == target:
                    return level
                
                for i in range(4):
                    digit = int(curr[i])
                    new_1 = str((digit - 1) % 10)
                    new_2 = str((digit + 1) % 10)
                    new_1 = curr[:i] + new_1 + curr[i+1:]
                    new_2 = curr[:i] + new_2 + curr[i+1:]

                    if new_1 not in visited:
                        visited.add(new_1)
                        queue.append(new_1)
                    
                    if new_2 not in visited:
                        visited.add(new_2)
                        queue.append(new_2)
            level += 1


        return -1
    


        

        


        