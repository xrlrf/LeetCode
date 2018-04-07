class Solution:
    def twoSum(self,nums,target):
        size = len(nums)
        for i in range(size):
            for j in range(i+1,size):
                if(nums[i] + nums[j] == target):
                    return i,j
        return 0,0

if __name__ == "__main__":
    nums = [2,7,11,15,1,3,53,245]
    TwoSum = Solution()
    print TwoSum.twoSum(nums,56)