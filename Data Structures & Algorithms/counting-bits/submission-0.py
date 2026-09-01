class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0: return [0]
        if n == 1: return [0,1]

        out = [0,1]
        for i in range(2,n+1):
            p = math.floor(math.log2(i))
            sub = 2 ** p
            c = 1 + out[i-sub]
            out.append(c)
        return out
        