class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        for(string c:tokens){
            if(c=="+"){
                int a = st.top();
                st.pop();
                int b = st.top();
                st.pop();
                int res = a+b;
                st.push(res);
            }
            else if(c=="-"){
                int a = st.top();
                st.pop();
                int b = st.top();
                st.pop();
                int res = b-a;
                st.push(res);
            }
            else if(c=="*"){
                int a = st.top();
                st.pop();
                int b = st.top();
                st.pop();
                int res = a*b;
                st.push(res);
            }
            else if(c=="/"){
                int a = st.top();
                st.pop();
                int b = st.top();
                st.pop();
                int res = b/a;
                st.push(res);
            }
            else{
                st.push(stoi(c));
            }
        }
        return st.top();
    }
};
