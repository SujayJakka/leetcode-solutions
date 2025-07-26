class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "":
            return ""
        
        counter_t = Counter(t)
        l, r = 0, 0
        have, need = 0, len(counter_t)
        window = defaultdict(int)
        res, res_len = [-1, -1], float("inf")

        while r < len(s):
            
            window[s[r]] += 1
            
            if window[s[r]] == counter_t[s[r]]:
                have += 1
            
            while have == need:

                if r - l + 1 < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                window[s[l]] -= 1

                if s[l] in counter_t and window[s[l]] < counter_t[s[l]]:
                    have -= 1
                
                l += 1
            
            r += 1
        
        l, r = res
        
        return s[l:r+1] if res_len != float("inf") else ""









        



            



        
        