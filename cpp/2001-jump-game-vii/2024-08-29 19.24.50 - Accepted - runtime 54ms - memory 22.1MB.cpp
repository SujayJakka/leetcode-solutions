class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        queue<int> my_queue;
        my_queue.push(0);
        int farthest = 0;

        while(!my_queue.empty()){
            int i = my_queue.front();
            my_queue.pop();
            int start = max(i + minJump, farthest + 1);

            for(int j = start; j < min(int(s.size()), i + maxJump + 1); j++){
                if(s[j] == '0') {
                    my_queue.push(j);
                    if(j == s.size() - 1)
                    {
                        return true;
                    }
                }
            }

            farthest = i + maxJump;

        }

        return false;
        
    }
};