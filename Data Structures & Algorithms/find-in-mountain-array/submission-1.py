class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        cache = {}
        le = mountainArr.length()

        def get(k):
            if k in cache:
                return cache[k]
            cache[k] = mountainArr.get(k)
            return cache[k]

        # Find peak — compare mid with mid+1 only (avoids index -1)
        l, r = 0, le - 2
        while l <= r:
            m = l + (r - l) // 2
            if get(m) < get(m + 1):
                l = m + 1
            else:
                r = m - 1
        peak = l

        # Search ascending side [0, peak] (inclusive — peak may be target)
        l, r = 0, peak
        while l <= r:
            m = l + (r - l) // 2
            val = get(m)
            if val == target: return m
            elif val < target: l = m + 1
            else: r = m - 1

        # Search descending side [peak+1, le-1]
        l, r = peak + 1, le - 1
        while l <= r:
            m = l + (r - l) // 2
            val = get(m)
            if val == target: return m
            elif val < target: r = m - 1
            else: l = m + 1

        return -1