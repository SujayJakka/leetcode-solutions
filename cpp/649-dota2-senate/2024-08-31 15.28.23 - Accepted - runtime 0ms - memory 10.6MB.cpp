class Solution {
public:
    string predictPartyVictory(string senate) {
        queue<int> r;
        queue<int> d;

        for(int i = 0; i < senate.size(); i++){
            if(senate[i] == 'R'){
                r.push(i);
            }
            else{
                d.push(i);
            }
        }

        while(!r.empty() && !d.empty()){
            int my_index = -1;
            if(r.front() < d.front()){
                my_index = r.front();
                r.pop();
                r.push(my_index + senate.size());
                d.pop();
            }
            else{
                my_index = d.front();
                d.pop();
                d.push(my_index + senate.size());
                r.pop();
            }

        }

        if(!r.empty()){
            return "Radiant";
        }
        else{
            return "Dire";
        }
    }
};