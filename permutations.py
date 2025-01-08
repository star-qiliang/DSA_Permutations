class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def get_res(nums):
            if len(nums)==1:
                return [nums,]

            res_list = []
            for i in range(len(nums)):
                tmp_nums = nums[:i] + nums[i+1:]
                tmp_list = get_res(tmp_nums)
                tmp_list = [[nums[i],]+x for x in tmp_list]
                res_list+=tmp_list

            return res_list

        res_list = get_res(nums)
        return res_list