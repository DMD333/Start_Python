# # SYNTAX looks like this   [ ____ for ____ in ____] -- > example of LIST COMPREHENSION
# # --> It takes one list and generate another list
# new_list = [1, 2, 3]
# multiply_list = [x * 10 for x in new_list]
# print(multiply_list)
#
# # --------------------------------------------
# name = 'daniel'
# z = [z.upper() for z in name]
# print(z)
#
# # --------------------------------------------
# mare = list(range(1, 6))
# multiplu = [a * 10 for a in mare]
# print(multiplu)
#
# # --------------------------------------------
# numere =[1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]
# turn_to_strings = [str(x) for x in numere]
# print(turn_to_strings)
# print(type(turn_to_strings))
#
# # --------------------------------------------
# numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = [x for x in numere if x % 2 == 0]
# print(even_numbers)
#
# # ----------------------------------------------
# only_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_numbers = [x * 2 if x % 2 != 0 else x / 2 for x in only_numbers]
# print(odd_numbers)
#
# # ----------------------------------------------
# answer1 = [val for val in [1, 2, 3, 4] if val in [3, 4, 5, 6]]
# print(answer1)
#
#
# answer2 = [a[::-1].lower() for a in ['Elie', 'Tim', 'Matt']]
# print(answer2)
#
# # -------------------------------------------------
# answer = [name for name in 'amazing' if name not in ['a', 'e', 'i', 'o', 'u']]
# print(answer)

# -------------------------------------------------- NESTED LISTS
# first_list = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# print(first_list)
#
# answer = [print(x) for x in first_list for z in range(1)]
#
# another_answer = [i for i in range(1, 4) for num in range(1, 4)]
# print(another_answer)

# # ----------------------------------------------------
# compreh_list = [[x for x in range(0, 3)] for z in range(0, 3)]
# print(compreh_list)
