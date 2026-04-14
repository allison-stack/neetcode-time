class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # want: [2*4*6, 1*4*6, 1*2*6, 1*2*4]
        # [2*4*6, 4*6, 6, 1]
        # [1, 1, 1*2, 1*2*4]
        first = [1]
        second = [1]
        res_first = 1
        res_second = 1
        l = len(nums) - 1
        res = []
        for i in range(l):
            first.append(res_first * nums[i])
            second.append(res_second * nums[l - i])
            res_first *= nums[i]
            res_second *= nums[l - i]
        for j in range(len(nums)):
            res.append(first[j] * second[l - j])
        return res






        