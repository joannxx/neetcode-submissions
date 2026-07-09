class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        op = []
        j = 0
        while i < len(nums):
            product = 1
            j = 0
            while j < len(nums):
                if j != i:
                    product *= nums[j]
                j+= 1
            op.append(product)
            i += 1

        return op
                
                    

           

            
            
            
        