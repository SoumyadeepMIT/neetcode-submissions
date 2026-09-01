class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.ls = []
        for i in nums:
            if i in self.ls:
                return True
            self.ls.append(i)
        return False