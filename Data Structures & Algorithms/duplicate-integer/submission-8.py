class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)
        n = len(nums)
        m = len(unique)
        return n>m