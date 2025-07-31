class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        zipped_list = list(zip(nums, cost))
        zipped_list = sorted(zipped_list)

        # prefix and suffix arrays
        prefix_arr_cost, suffix_arr_cost = [0], []
        curr_cost = 0
        for i in range(len(zipped_list) - 1):
            curr_cost += zipped_list[i][1]
            prefix_arr_cost.append(curr_cost)
        curr_cost = 0
        for i in range(len(zipped_list) - 1, -1, -1):
            curr_cost += zipped_list[i][1]
            suffix_arr_cost.append(curr_cost)
        suffix_arr_cost = suffix_arr_cost[::-1]

        # Find answer
        res = float("inf")

        base = zipped_list[0][0]
        curr = 0
        for i in range(len(zipped_list)):
            curr += ((zipped_list[i][0] - base) * zipped_list[i][1])
        res = min(res, curr)
        
        for i in range(1, len(zipped_list)):
            diff_base = zipped_list[i][0] - zipped_list[i - 1][0]
            curr += (prefix_arr_cost[i] * diff_base)
            curr -= (suffix_arr_cost[i] * diff_base)
            res = min(curr, res)
        
        return res

