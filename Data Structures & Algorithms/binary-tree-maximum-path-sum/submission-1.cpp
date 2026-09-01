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
        int lv = calc(root->left);
        int rv = calc(root->right);
        int a = max(root->val+lv,root->val+rv);
        int b = max(a,root->val);
        int c = max(b, lv+rv+root->val);
        res=max(res,c);
        int d = max(max(lv,rv), 0);
        return root->val+d;
    }
    int maxPathSum(TreeNode* root) {
        res=INT_MIN;
        calc(root);
        return res;
    }
};
