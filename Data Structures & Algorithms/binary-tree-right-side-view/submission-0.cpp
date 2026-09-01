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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        if(!root){
            return res;
        }
        queue<TreeNode*> qu;
        qu.push(root);
        
        while(!qu.empty()){
            int s = qu.size();
            for(int i=0;i<s;i++){
                TreeNode* t = qu.front();
                qu.pop();
                if(i==s-1){
                    res.push_back(t->val);
                }
                if(t->left){
                    qu.push(t->left);
                }
                if(t->right){
                    qu.push(t->right);
                }
            }
        }
        return res; 
    }
};
