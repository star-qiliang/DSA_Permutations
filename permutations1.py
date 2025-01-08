
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:

#         def get_sub_combination(sub_list):
#             if not sub_list:
#                 return [[]]
            
#             if len(sub_list)==1:
#                 return [sub_list, ]
            
#             cur = sub_list[0]
#             res_list = get_sub_combination(sub_list[1:])
#             final_list = []
#             for tmp_list in res_list:
#                 # print("tmp_list:", tmp_list)
#                 for i in range(len(tmp_list)+1):
#                     new_res = tmp_list[:i] + [cur,] + tmp_list[i:]
#                     final_list.append(new_res)

#             return final_list

#         res_list = get_sub_combination(nums)
#         return res_list




def get_combination(input_list):
    
    def get_sub_combination(sub_list):
        if not sub_list:
            return [[]]
        
        if len(sub_list)==1:
            return [sub_list, ]
        
        cur = sub_list[0]
        res_list = get_sub_combination(sub_list[1:])
        final_list = []
        for tmp_list in res_list:
            # print("tmp_list:", tmp_list)
            for i in range(len(tmp_list)+1):
                new_res = tmp_list[:i] + [cur,] + tmp_list[i:]
                final_list.append(new_res)


        return final_list

    res_list = get_sub_combination(input_list)
    return res_list



def main():

    input_list = []
    res_list  = get_combination(input_list)
    print("input_list:", input_list)
    print("res_list:", res_list)
    print()


    input_list = [1]
    res_list  = get_combination(input_list)
    print("input_list:", input_list)
    print("res_list:", res_list)
    print()

    input_list = [1,2,3]
    res_list  = get_combination(input_list)
    print("input_list:", input_list)
    print("res_list:", res_list)
    print()


    input_list = [1,2,3,4]
    res_list  = get_combination(input_list)
    print("input_list:", input_list)
    print("res_list:", res_list)
    print()


    input_list = [4,29,20,1,45]
    res_list  = get_combination(input_list)
    print("input_list:", input_list)
    print("res_list:", res_list)
    print()


if __name__=="__main__":
    main()
    print("\nDone!\n")
