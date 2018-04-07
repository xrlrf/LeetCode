class Solution(object):
    """
    :type nums:List[int]
    :type target:int
    :rtype: List[int]
    """
    def twoSum(self,nums,target):
        for i,num in enumerate(nums):
            if target - num in nums and nums[i] != target - num:
                return [i,nums.index(target - num)]
        return [] # no sum


if __name__ == '__main__':  
    TwoSum = Solution()                                  
    nums = [2,7,11,15,1,3,53,245]
    print TwoSum.twoSum(nums,56)
    