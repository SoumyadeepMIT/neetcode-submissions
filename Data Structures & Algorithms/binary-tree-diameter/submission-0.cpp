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
        if(!root){
            return 0;
        }
        int a = calc(root->left);
        int b = calc(root->right);
        res=max(res, a+b);
        return max(a,b)+1;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        res=0;
        calc(root);
        return res;
    }
};
