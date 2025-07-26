/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    unordered_map<int, int> my_map;

    bool isEvenOddTree(TreeNode* root) {

        return helper_function(0, root);
    }

    bool helper_function(int level, TreeNode* node){
        if(node == nullptr){
            return true;
        }
        
        if(level % 2 == 0 && node->val % 2 == 1){
            if(my_map.find(level) != my_map.end()){
                if(my_map[level] < node->val){
                    my_map[level] = node->val;
                    if(!helper_function(level + 1, node->left)){
                        return false;
                    }
                    if(!helper_function(level + 1, node->right)){
                        return false;
                    }

                    return true;
                }
            }
            else{
                my_map[level] = node->val;
                if(!helper_function(level + 1, node->left)){
                    return false;
                }
                if(!helper_function(level + 1, node->right)){
                    return false;
                }
                return true;
            }

        }
        else if(level % 2 == 1 && node->val % 2 == 0){
            if(my_map.find(level) != my_map.end()){
                if(my_map[level] > node->val){
                    my_map[level] = node->val;
                    if(!helper_function(level + 1, node->left)){
                        return false;
                    }
                    if(!helper_function(level + 1, node->right)){
                        return false;
                    }

                    return true;
                }

            }
            else{
                my_map[level] = node->val;
                if(!helper_function(level + 1, node->left)){
                    return false;
                }
                if(!helper_function(level + 1, node->right)){
                    return false;
                }
                return true;
            }

        }
        return false;
    }
};