def removeDuplicates(self, nums):
    if len(nums) == 0:
        return 0
    k = 1
    dupe = 0
    prev = nums[0]

    for i in range(1, len(nums)):
        if nums[i] == prev:
            dupe+=1
        else:
            dupe = 0
        if dupe <=1:
            nums[k] = nums[i]
            k+=1
            prev = nums[i]
    return k
