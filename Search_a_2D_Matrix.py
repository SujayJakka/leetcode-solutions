class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        row = None

        #binary search for rows
        def binary_search_rows(l, r, target):

            while l <= r:

                mid = (l+r) // 2

                if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                    return mid
                elif matrix[mid][0] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            
            return mid
        

        def binary_search_cols(l, r, target, row_index):

            while l <= r:
            
                mid = (l+r) // 2

                if matrix[row_index][mid] == target:
                    return True
                elif matrix[row_index][mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return False
        


        row_index = binary_search_rows(0, m-1, target)
        return binary_search_cols(0, n-1, target, row_index)



        


            


        
