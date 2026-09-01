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
    int res;
    int calc(TreeNode* root){
        if(!root)
            return 0;
        int lv = max(calc(root->left), 0);
        int rv = max(calc(root->right), 0);
        res=max(res,root->val+lv+rv);
        return root->val+max(lv,rv);
    }
    int maxPathSum(TreeNode* root) {
        res=INT_MIN;
        calc(root);
        return res;
    }
};
