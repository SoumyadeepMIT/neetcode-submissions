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
    int good(TreeNode* root, int maxv){
        if(!root){
            return 0;
        }
        if(root->val>=maxv){
            res++;
            maxv = root->val;
        }
        good(root->left, maxv);
        good(root->right, maxv);
    }
    int goodNodes(TreeNode* root) {
        res=0;
        good(root, INT_MIN);
        return res;
    }
};
