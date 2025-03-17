# # #elif program to check temperature.
# # a = int(input("enter temperature in celsius : "))
# # if a < 0:
# #     print("freezing")
# # elif a > -1 and a < 15:
# #     print("cold")
# # else:
# #     print("hot")
#
# ##########
# #program to print odd numbers from m - n. output should be returned from a function
# # def check_oddnumbers(start_number, end_number):
# #     odd_numbers = []
# #     for i in range(start_number, end_number+1):
# #         if i % 2 != 0:
# #             odd_numbers += [i]
# #     return odd_numbers
# # start_number = int(input())
# # end_number = int(input())
# # odd_numbers = check_oddnumbers(start_number, end_number)
# # print(odd_numbers)
#
# #######################
# Write a function calculate_bonus(employee_data, bonus_percentage) that takes:
# employee_data: A list of dictionaries, where each dictionary contains:
# "name": (string) Employee's name
# "salary": (float) Employee's salary
# "performance": (string) Employee's performance rating, which can be "excellent", "good", or "average"
# bonus_percentage: A dictionary that maps performance ratings to bonus percentages.
# example input: employees = [
#     {"name": "Alice", "salary": 50000, "performance": "excellent"},
#     {"name": "Bob", "salary": 60000, "performance": "good"},
#     {"name": "Charlie", "salary": 45000, "performance": "average"},
# ]
# bonus_percentage = {
#     "excellent": 20,
#     "good": 10,
#     "average": 5
# }
# Requirements:
# The function should calculate the bonus amount for each employee based on their performance.
# The function should return a new list of dictionaries, where each dictionary contains:
# expected output : [
#     {"name": "Alice", "salary": 50000, "bonus": 10000.0},
#     {"name": "Bob", "salary": 60000, "bonus": 6000.0},
#     {"name": "Charlie", "salary": 45000, "bonus": 2250.0},
# ]
# import json # to take dictionary inputs
# def calculate_bonus(employee_data, bonus_percentage):
#     result = []
#     for employee in employee_data:
#         performance = employee['performance']
#         bonus = employee['salary']/bonus_percentage[performance]
#         del employee['performance']
#         employee['bonus'] = bonus
#         result.append(employee)
#     return result
#
#
# employee_data = input()
# employee_data = json.loads(employee_data)
# bonus_percentage = input()
# bonus_percentage = json.loads(bonus_percentage)
# bonus_results = calculate_bonus(employee_data, bonus_percentage)
# print(bonus_results)

