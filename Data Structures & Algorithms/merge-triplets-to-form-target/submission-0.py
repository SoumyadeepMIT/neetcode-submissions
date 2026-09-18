class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        n = len(triplets)
        m0, m1, m2 = 0,0,0
        for t in triplets:
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                continue
            m0 = max(m0, t[0])
            m1 = max(m1, t[1])
            m2 = max(m2, t[2])
        return (m0 == target[0]) and (m1 == target[1]) and (m2 == target[2])