class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        curr_triplet = [0] * 3

        for triplet in triplets:

            a, b, c = triplet

            if a <= target[0] and b <= target[1] and c <= target[2]:
                curr_triplet = [max(a, curr_triplet[0]), max(b, curr_triplet[1]), max(c, curr_triplet[2])]
        
        return True if curr_triplet == target else False
        