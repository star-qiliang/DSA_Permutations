class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def get_combination(a_list):
            if not a_list:
                return [[]]
            if len(a_list)==1:
                return [a_list,]

            res_list = []
            for i in range(len(a_list)):
                tmp_list = a_list[:i] + a_list[i+1:]
                tmp_res_list = get_combination(tmp_list)
                tmp_res_list = [[a_list[i]]+x for x in tmp_res_list]
                res_list += tmp_res_list

            return res_list

        res_list = get_combination(nums)

        return res_list

