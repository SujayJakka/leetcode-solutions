class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int l = 0;
        int window_size = cardPoints.size() - k;
        int r = window_size - 1;
        int curr_sum = accumulate(cardPoints.begin(), cardPoints.begin() + window_size, 0);
        int min_value = curr_sum;

        while(r + 1 < cardPoints.size()){
            curr_sum += cardPoints[r + 1];
            curr_sum -= cardPoints[l];

            min_value = min(curr_sum, min_value);

            r += 1;
            l += 1;
            
        }

        int total = accumulate(cardPoints.begin(), cardPoints.end(), 0);
        return total - min_value;
    }
};