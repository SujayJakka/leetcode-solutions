class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        DP_cache = set()

        def recursive_method(s1_ptr, s2_ptr):
            if s1_ptr == len(s1) and s2_ptr == len(s2):
                return True
            
            if (s1_ptr, s2_ptr) in DP_cache:
                return False
            
            if s1_ptr < len(s1) and s1[s1_ptr] == s3[s1_ptr + s2_ptr] and recursive_method(s1_ptr + 1, s2_ptr):
                return True
            
            if s2_ptr < len(s2) and s2[s2_ptr] == s3[s1_ptr + s2_ptr] and recursive_method(s1_ptr, s2_ptr + 1): 
                return True

            DP_cache.add((s1_ptr, s2_ptr))
            return False
        
        return recursive_method(0, 0)
        