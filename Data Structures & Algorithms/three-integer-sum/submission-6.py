class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the list to make skipping duplicates easier!!
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            # use two pointers to find other two elements in triplet
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # only need to increment one of the pointers because the above conditions will cause the other pointer will automatically update
                    l += 1
                    # skip duplicates
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
                

        