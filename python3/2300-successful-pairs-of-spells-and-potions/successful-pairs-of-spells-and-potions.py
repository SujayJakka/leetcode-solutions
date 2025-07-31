class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        potions = sorted(potions)

        def binary_search(l, r, success, spell):

            curr = -1
            while l <= r:
                mid = (l + r) // 2
                if spell * potions[mid] >= success:
                    curr = mid
                    r = mid - 1
                else:
                    l = mid + 1
            
            return 0 if curr == -1 else len(potions) - curr

        for spell in spells:
            pairs.append(binary_search(0, len(potions) - 1, success, spell))
        return pairs
        