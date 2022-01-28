# d = dict(a = 1, b = 2, c = 3)
# # or
# name = {'first': 'Daniel', 'last': 'Dumitru'}
#
# print(name['first'])   # Print one value from the dictionary
#
# print(name.values())  # Print all the values inside the dictionary
#
# full_name = name['first'] + ' ' + name['last']
# print(full_name)
#
#
# # ---------------------------------------------------------------
# # Accessing all the values inside of DICTIONARIES use: --> .values()
# # EXEMPLE   -->   for item in shop.values():
#
# instructor = {'first name': 'Dumitru', 'last name': 'Daniel', 'Age': 30, 'country': 'Romania', 'city': 'Bucharest'}
# for item in instructor.values():  # Print all the items inside the dictionary
#     print(item)
#
#
# # ------------------------------------------------------------------
# # Another way of printing KEYS and VALUES of Dictionaries using:  -->  .items()
# # EXEMPLE
personal_info = {'first name': 'Dumitru', 'last name': 'Daniel', 'Age': 30, 'country': 'Romania', 'city': 'Bucharest'}
for x, item in personal_info.items():  # Print all the items inside the dictionary
    print(x,':', item)

# # ---------------------------------------------------------------------
# # Calculating the SUM of dictionary values
# dictionr = {1: 5, 2: 7, 3: 12, 4: 18, 5: 18}
# var = sum(v for v in dictionr.values())
#
# print(var)
#
#
# # --------------------------------------------------------------------
# # Testing if a KEY is in Dictionary
# info = {'first name': 'Dumitru', 'last name': 'Daniel', 'Age': 30, 'country': 'Romania', 'city': 'Bucharest'}
# valoare = 'first name' in info
# print(valoare)
#
# # Testing if a value is in Dictionary
# test_name = 'Daniel' in info.values()
# print(test_name)
#
# # -----------------------------------------------------------------------
# # DICTIONARIES Methods
# # -----------------------------------------------------------------------
# d = dict(a = 1, b = 2, c = 3)
# # d.clear()
# print(d)
#
# # create unique copy of dictionary - EXAMPLE:
# dictionar = d.copy()
# print(dictionar)
# answer1 = dictionar is d      # it tests if the values are stored in the same place in the memory
# print(answer1)
#
# answer2 = dictionar == d      # it tests if the values from (dictionar) are equal with the values from (d)
# print(answer2)
#
# # ---------------------------------------------------------------------------
# # Create key-values pairs from comma separated values:
# {}.fromkeys(('a', 'b'))  # {'a': 'b'}
# {}.fromkeys(['email'], 'unknown')  # {'Email': 'unknown'} --> sets all the keys with 'unknown' values
# {}.fromkeys('a', [1, 2, 3, 4, 5])  # {'a': [1, 2, 3, 4, 5]}
#
# new_user = {}  # declare an empty dictionary
# print(new_user)
#
# # ---------------------------------------------------------------------------
# # How to get values printed from dictionaries :  -->   .get(key)
# info = {'first name': 'Dumitru', 'last name': 'Daniel', 'Age': 30, 'country': 'Romania', 'city': 'Bucharest'}
# a = info.get('first name')
# print(a)
#
#
# # ---------------------------------------------------------------------------
# # Deleting values from a coresponding key :  --> pop()
# # EXAMPLE:
# d = dict(a = 1, b = 2, c = 3, d = 4, e = 5, f = 6, g = 7, h = 8)
# d.pop('a')    # Remove values from corespondent key
# d.pop('e')    # KeyError
# d.popitem()   # Removes random key in a dictionary
# print(d)
#
#
# # ---------------------------------------------------------------------------
# # UPDATE keys and values in a dictionary with another set of key values pairs
# first = dict(a = 1, b = 2, c = 3, d = 4, e = 5, f = 6, g = 7, h = 8)
# second = {}
# second.update(first)
# print(second)
#
# second['a'] = 'AMAZING'
# print(second)
