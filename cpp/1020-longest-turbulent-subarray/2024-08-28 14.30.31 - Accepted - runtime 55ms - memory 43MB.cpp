class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        int r = 1;
        int res = 1;
        int curr_res = 1;

        string compare = "";

        while(r != arr.size()) {
            if((arr[r] < arr[r - 1]) && compare != ">") {
                compare = ">";
                curr_res = curr_res + 1;
                res = max(curr_res, res);
                r = r + 1;
            }
            else if((arr[r] > arr[r - 1]) && compare != "<") {
                compare = "<";
                curr_res = curr_res + 1;
                res = max(curr_res, res);
                r = r + 1;
            }
            else {
                if(arr[r] == arr[r - 1]){
                    r += 1;
                }
                curr_res = 1;
                compare = "";
            }
        }

        return res;
    }
};