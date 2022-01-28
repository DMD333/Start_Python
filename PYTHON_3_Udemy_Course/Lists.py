# A List it's a collection of grouping of items
item1 = 'bananas'
item2 = 'lego set'
# we can do it shorter -->>

tasks = ['Install Python', 'Learn Python', 'Take a break']
length = len(tasks)  # Shows the length of the List
print(length)

# Accessing specific element from List wi the square brackets and position number of element [0] -->first element of List
python = tasks[0]
print(python)
python = tasks[-1]
print(python)

if 'Install Python' in tasks:
    print(True)

array = list(range(1, 8))  # Another way to built a function called -->  list()
print(array)

r = range(1, 4)
r = list(r)
print(r)

# Accessing all values in a List
colors = ['purple', 'teal', 'magenta', 8.9]
for x in colors:
    print(x)

# --------------------------------------------------------------------------------
# While Loop
i = 0
while i < len(colors):
    print(colors[i])
    i += 1

# --------------------------------------------------------------------------------
#  if you want to add 1 item to the list use : --> .append()
motociclete = ['suzuki', 'honda', 'davidson']
masini = ['dacia', 'renault', 'BMW']
masini.append(motociclete)
print(masini)

# --------------------------------------------------------------------------------
#  extend()  --> add to the end of a list all values passed to extend
#  if you want to add more items to the list use : --> .extend()
bloc = ['A1', 'A2', 'B1', 'B2']
casa = ['C1', 'C2']
bloc.extend(casa)
print(bloc)

# --------------------------------------------------------------------------------
#  if we want to add item wherever in the list use : --> .insert(index, 'value')
curcubeu = ['purple', 'teal', 'magenta', 8.9]
curcubeu.insert(2, 'Blue')
print(curcubeu)

#  insert into a list inside another list
elicopter = ['Croco_2', 'Croco_7', 'Apash_91']
armata = ['Soldat_1', 'Soldat_2', 'Soldat_3', 'soldat_5', 'Soldat_6']
elicopter.append(armata)
print(elicopter)
elicopter[3].append('Soldat_4')
print(elicopter)

# -------------------------------------------------------------------------------
#  Remove all elements inside the list with function --> .clear()
elicopter.clear()
print(elicopter)

# -------------------------------------------------------------------------------
#  Remove single element from list items use : --> .pop('index')
armata.pop()
print(armata)

#  If do not insert index it will remove last item from list
armata.pop(1)
print(armata)

# -------------------------------------------------------------------------------
armata.remove('soldat_5')  # Removes a specific value that we give
# : --> .remove('item_name') --> if not found throw error
print(armata)

# -------------------------------------------------------------------------------
# index position to be found regarding element in the list
armata = ['Soldat_1', 'Soldat_2', 'Soldat_2', 'Soldat_3', 'soldat_5', 'Soldat_6']
nume = armata.index('Soldat_1')
print(nume)

nume = armata.index('Soldat_2', 2)  # Search 'Soldat_2' after position 2 in List
print(nume)

nume = armata.index('Soldat_2', 2, 5)  # Search 'Soldat_2' between position 2 and 5 in List
print(nume)

# ---------------------------------------------------------------------------------
# counting the elements inside the list with .count('item_to_count')
count_1 = armata.count('Soldat_2')
print('We found:', count_1)

# -----------------------------------------------------------------------------------
# reversing the list with .reverse()
print(armata)
armata.reverse()
print(armata)

# -----------------------------------------------------------------------------------
# sorting list with .sort()
armata.sort()
print(armata)

# ------------------------------------------------------------------------------------
# join is a string method / convert list to string -->  .join(list)
arma = 'militar '.join(armata)
print(arma)

# --------------------------------------------------------------------------------------
# make new lists from old list using Slices -->  list[start:end:step]

armata = ['Soldat_1', 'Soldat_2', 'Soldat_2', 'Soldat_3', 'soldat_5', 'Soldat_6']
print(armata[1:5])  # prints items from list from index 2 to index 4
print(armata[1:5:2])  # prints items from list from index 2 to index 4  | din 2 in 2

# --------------------------------------------------------------------------------------
# swapping values in list

armata[0], armata[1] = armata[1], armata [0]
print(armata)