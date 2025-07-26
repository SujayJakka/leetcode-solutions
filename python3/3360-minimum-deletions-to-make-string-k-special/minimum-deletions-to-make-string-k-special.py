class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        
        counter = Counter(word)
        res = len(word)

        for a in counter:
            deletions = 0
            for b in counter:
                if counter[a] > counter[b]:
                    deletions += counter[b]
                elif counter[b] - counter[a] > k:
                    deletions += (counter[b] - counter[a] - k)
        
            res = min(res, deletions)

        return res

        
        