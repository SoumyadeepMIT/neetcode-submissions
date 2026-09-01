class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int res=0;
        int n = heights.size();
        stack<pair<int,int>> st;
        for(int i=0;i<heights.size();i++){
            int f=i;
            while(!st.empty() && st.top().second>heights[i]){
                pair<int,int> rec = st.top();
                st.pop();
                int a=rec.second*(i-rec.first);
                res=max(res,a);
                f = rec.first;
            }
            st.push({f,heights[i]});
        }
        while(!st.empty()){
            pair<int,int> rec = st.top();
            int a = rec.second*(n-rec.first);
            res=max(res,a);
            st.pop();
        }
        return res;
    }
};
