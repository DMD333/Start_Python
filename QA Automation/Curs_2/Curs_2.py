nume = "Dumitru"
prenume = "Daniel"

print(' numele meu ete {}'.format(nume))

print(f'numele meu este {nume} iar prenumele este {prenume}')

#--------------------------------------------------------------------

cuvant = "Ana are mere"
print(len(cuvant))
print("Prima pozitie", cuvant[0])

print("Afisare numere din 2 in 2: ", cuvant[::2])

print("Afisarea sirului invers", cuvant[::-1])

numele_meu = "Daniel"
print(numele_meu.upper()) #--> face numele cu litere de tipar

print((numele_meu.capitalize())) #--> face prima litera sa fie de tipar

print(nume.find('u')) #--> ne spune pe a cata pozitie se afla caracterul respectiv din interorul stringului

print(cuvant.replace('Ana', "Iulia"))

a = input("Primul numar: ")
b = input("Al doilea numar: ")
print(int(a) + int(b)) #--> numerele citite de la tastatura sunt STRING si  sunt convertite in tip INT pentru a putea fi efectuate operatii matematice

c = int(input("Numar: "))
d = int(input("Alt numar: "))
print(c+d)

#----------------------------------------------------------------------
# == arata egalitatea dintre 2 elemente
# >= mai mare sau egal
# <= mai mic sau egal
# != nu e egal

assert a == b
assert 18 == 54 or 12 > 10
assert "in" in "Alina"