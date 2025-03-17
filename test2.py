# '''
# write a function which returns a string (huffmen encoding)
# input : string(lowercase)
# eg: aabbcc, abcabc
# output : a2b2c2
# '''
#
# def freq_encode(s):
#     count = {}
#     for i in s:
#         count[i] = count.get(i, 0) + 1
#         # if i not in count:
#         #     count.get(i, 1)
#         #     print(count)
#         # else:
#         #     count[i]+= 1
#     result_string = ""
#     for key, value in count.items():
#         result_string += key+str(value)
#     return result_string
#
#
#
# if __name__ == '__main__':
#     s1 = "aabbbcc"
#     res1 = freq_encode(s1)
#     print(res1)


# // this is the function signature for sum of elements in the array
#
#
# int sumOfElements(int* array,int len){
#
#     // write your code here
#
# }
# def sum_of_elements(array):
#     return (sum(array))

#
# // this is the function signature for product of elements in the array
#
# int productOfElements(int*  array,int len){
#
# // write your code here
#
# }
# def product_of_elements(array):
#     a = 1
#     for i in array:
#         a = a*i
#     return a
# # // this is the function for returning max element in the arrray
# #
# # int maximum(int* array,int len){
# #
# # // write your code here
# #
# # }
# def maximum(array):
#     return max(array)
# #
# # // this is the function for returnin min element in the arrra
# #
# # int minimum(int* array,int len){
# #
# #     // write your code here
# # }
# def mimimum(array):
#     return min(array)
# # call these functions from main
# # write all functions in one program and send the entire cpp file to me
# if __name__ == '__main__':
#     array = [4, 6, 3, 9]
#     print(sum_of_elements(array))
#     print(product_of_elements(array))
#     print(maximum(array))
#     print(mimimum(array))
# find and list all numbers that appear an odd number of times in a given sequence of space-separated numbers.
# The output should be a sorted list of these numbers.
# num = list(map(int, input().split()))
# occ_dict = {}
# for i in num:
#     occ_dict[i] = occ_dict.get(i, 0) + 1
# output = []
# for key, value in occ_dict.items():
#     if value % 2 != 0:
#         output.append(key)
# print(sorted(output))

# optimized code
#
# num = list(map(int, input().split()))
# no_dup = []
# result = []
# for i in num:
#     if i not in no_dup:
#         no_dup.append(i)
#         if num.count(i) % 2 != 0:
#             result.append(i)
# print(sorted(result))

# Given a list of integers, write a program to identify contiguous sub-list that has the largest sum and print the sub-list. Any non-empty slice of
# the list with step size 1 can be considered as contiguous sub-list.
# eg: For example, if the given list is [2, -4, 5, -1, 2, -3], then all the possible contiguous sub-lists will be,
# [2]
# [2, -4]
# [2, -4, 5]
# [2, -4, 5, -1]
# [2, -4, 5, -1, 2]
# [2, -4, 5, -1, 2, -3]
# [-4]
# [-4,5]
# [-4, 5, -1]
# [-4, 5, -1, 2]
# [-4, 5, -1, 2, -3]
# [5]
# [5, -1]
# [5, -1, 2]
# [5, -1, 2, -3]
# [-1]
# [-1, 2]
# [-1, 2, -3]
# [2]
# [2, -3]
# [-3]
#Among the above contiguous sub-lists, the contiguous sub-list [5, -1, 2] has the largest sum which is 6. So the output should be 5 -12
# input_list = list(map(int, input().split()))
# sliced_list = input_list
# max_sum = []
# for i in range(len(input_list)):
#     for j in range(len(sliced_list)):
#         temp_list = sliced_list[:j+1]
#         if sum(temp_list) > sum(max_sum):
#             max_sum = temp_list
#     sliced_list = sliced_list[1:]
# print(max_sum)
