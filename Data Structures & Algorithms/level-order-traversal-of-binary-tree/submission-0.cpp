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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if(!root){
            return res;
        }
        queue<TreeNode*> qu;
        qu.push(root);
        
        while(!qu.empty()){
            int s = qu.size();
            vector<int> temp;
            for(int i=0;i<s;i++){
                TreeNode* t = qu.front();
                qu.pop();
                temp.push_back(t->val);
                if(t->left){
                    qu.push(t->left);
                }
                if(t->right){
                    qu.push(t->right);
                }
            }
            res.push_back(temp);
        }
        return res;     
    }
};
