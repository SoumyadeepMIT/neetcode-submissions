class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        n = len(nums)
        freq = [[] for _ in range(n+1)]
        for n in nums:
            if n in count.keys():
                count[n] += 1
            else:
                count[n] = 1
        for n, cnt in count.items():
            freq[cnt].append(n)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k: return res