class Solution(object):
    """
    :type nums:List[int]
    :type target:int
    :rtype: List[int]
    """
    def twoSum(self,nums,target):
        num_to_index = {}   # key is number,value is index in nums
        for i,num in enumerate(nums):
            if target - num in num_to_index:
                return [i,num_to_index[target-num]]

            num_to_index[num] = i
        return [] # no sum


if __name__ == '__main__':  
    TwoSum = Solution()                                  
    nums = [2,7,11,15,1,3,53,245]
    print TwoSum.twoSum(nums,56)
    