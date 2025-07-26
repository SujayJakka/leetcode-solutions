class Solution {
public:
    int eliminateMaximum(vector<int>& dist, vector<int>& speed) {
        vector<int> times;
        for(int i = 0; i < dist.size(); i++){
            int time = ceil(double(dist[i]) / double(speed[i]));
            times.push_back(time);
        }

        sort(times.begin(), times.end());
        int res = 0;
        for(int i = 0; i < times.size(); i++){
            int curr = times[i];
            if(curr <= i){
                return res;
            }
            res++;
        }
        return res;
    }
};