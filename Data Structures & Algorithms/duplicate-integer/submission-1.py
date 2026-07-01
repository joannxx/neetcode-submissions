class Solution:
    def hasDuplicate(self,nums):
        sets = set(nums)
        if len(nums) == len(sets): # check if lengths are same
            return False
        else:
            return True


nums = [1,2,3,3]
sol = Solution()
print(sol.hasDuplicate(nums))
