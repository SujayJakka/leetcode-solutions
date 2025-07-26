class Solution {
public:
    vector<vector<int>> my_grid;

    int getMaximumGold(vector<vector<int>>& grid) {

        my_grid = grid;
        int res = 0;

        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[0].size(); j++){
                res = max(dfs(i, j), res);
            }
        }

        return res;
        
    }

    int dfs(int i, int j){
        if(i < 0 || i == my_grid.size() || j < 0 || j == my_grid[0].size()){
            return 0;
        }
        if(my_grid[i][j] == 0){
            return 0;
        }

        array<tuple<int, int>, 4> directions = {make_tuple(i + 1, j), make_tuple(i - 1, j), make_tuple(i, j + 1), make_tuple(i, j - 1)};
        int temp = my_grid[i][j];
        my_grid[i][j] = 0;
        int res = 0;

        for(tuple<int, int> direction : directions){
            res = max(dfs(get<0>(direction), get<1>(direction)), res);
        }

        my_grid[i][j] = temp;
        return res + my_grid[i][j];

    }

    
};