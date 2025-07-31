class Solution:
    def getSmallestString(self, s: str) -> str:

        arr = list(s)

        for i in range(1, len(arr)):
            if int(arr[i]) < int(arr[i - 1]):
                if (int(arr[i]) % 2 == 0 and int(arr[i - 1]) % 2 == 0) or (int(arr[i]) % 2 == 1 and int(arr[i - 1]) % 2 == 1):
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
                    break
        
        return "".join(arr)

                
        