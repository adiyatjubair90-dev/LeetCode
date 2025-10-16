def majorityElement(self, nums):
    nums.sort()
    k = len(nums) / 2
    return nums[k]
