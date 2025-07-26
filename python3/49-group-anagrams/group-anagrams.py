class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_map = defaultdict(list)

        def helper(s):
            array_1 = [0] * 26
            for char in s:
                array_1[ord(char) - 97] += 1
            return tuple(array_1)
        
        for i, s in enumerate(strs):
            representation = helper(s)
            h_map[representation].append(s)
        
        return list(h_map.values())

        



                        
                    
                

