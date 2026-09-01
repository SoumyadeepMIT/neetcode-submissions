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
    int i =0;
    unordered_map<int,int> um;
    TreeNode* build(vector<int>& preorder,int l,int r){
        if(l>r){
            return nullptr;
        }
        int v = preorder[i++];
        int mid = um[v];
        TreeNode* root = new TreeNode(v);
        root->left = build(preorder,l,mid-1);
        root->right = build(preorder,mid+1,r);
        return root;
    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        for(int i=0;i<inorder.size();i++){
            um[inorder[i]]=i;
        }
        TreeNode* root = build(preorder,0,preorder.size()-1);
        return root;
    }
};
