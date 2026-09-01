class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.dic = {}
        for i in range(len(nums)):
            com = target - nums[i]
            if com in self.dic:
                return [self.dic[com], i]
            self.dic[nums[i]] = i

        return []