class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        sort(points.begin(), points.end());
        int res = 1;
        int min_boundary = points[0][0];
        int max_boundary = points[0][1];
        for(int i = 1; i < points.size(); i++){
            if(points[i][0] <= max_boundary){
                min_boundary = points[i][0];
                max_boundary = min(max_boundary, points[i][1]);
            }
            else{
                res += 1;
                min_boundary = points[i][0];
                max_boundary = points[i][1];
            }
        }
        return res;
        
    }
};