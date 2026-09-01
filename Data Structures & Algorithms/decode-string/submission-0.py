class Solution:
    def decodeString(self, s: str) -> str:
        count_st = []
        str_st = []
        k = 0
        cur = ""
        for c in s:
            if c.isdigit():
                k = k*10 + int(c)
            elif c == '[':
                count_st.append(k)
                str_st.append(cur)
                k = 0
                cur = ""
            elif c == ']':
                temp = cur
                cur = str_st.pop()
                count = count_st.pop()
                cur = cur + (temp*count)
            else:
                cur += c
        return cur