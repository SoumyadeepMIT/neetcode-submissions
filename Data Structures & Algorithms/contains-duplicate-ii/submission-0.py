class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        n = len(nums)
        for i in range(min(n,k+1)):
            if nums[i] in dic.keys():
                return True
            dic[nums[i]] = i
        for i in range(k+1, n):
            num = nums[i-k-1]
            if num in dic.keys():
                if dic[num] <= i-k-1:
                    dic.pop(num, None)
            if nums[i] in dic.keys():
                return True
            dic[nums[i]] = i
        return False
            