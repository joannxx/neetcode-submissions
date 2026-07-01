class Solution:
    def hasDuplicate(self,nums):
        sets = set(nums)
        if len(nums) == len(sets): # check if lengths are same
            return False
        else:
            return True


