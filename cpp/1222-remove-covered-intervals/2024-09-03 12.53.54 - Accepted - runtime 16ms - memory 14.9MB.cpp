class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        int res = 0;
        int max_boundary = -1;
        for(int i = 0; i < intervals.size(); i++){
            if(i + 1 < intervals.size() && intervals[i][0] == intervals[i + 1][0]){
                res += 1;
            }
            else if(intervals[i][1] <= max_boundary){
                res += 1;
            }
            max_boundary = max(max_boundary, intervals[i][1]);
        }
        return intervals.size() - res;
        
    }
};