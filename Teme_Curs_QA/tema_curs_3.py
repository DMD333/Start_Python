
for x in range(1,21):
   if x == 4 or x == 13:
       print(f'{x} unlucky')
   elif x % 2 != 0:
       print(f'{x} is odd')
   else: print(f'{x} even')