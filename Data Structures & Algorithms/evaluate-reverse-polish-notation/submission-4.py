class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for c in tokens:
            if c == '+':
                t1 = st.pop()
                t2 = st.pop()
                st.append(t1+t2)
            elif c == '-':
                t1 = st.pop()
                t2 = st.pop()
                st.append(t2-t1)
            elif c == '*':
                t1 = st.pop()
                t2 = st.pop()
                st.append(t1*t2)
            elif c == '/':
                t1 = st.pop()
                t2 = st.pop()
                st.append(int(t2/t1))
            else:
                st.append(int(c))
        return st[-1]