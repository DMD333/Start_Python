def adunare(nr_1, nr_2):
    print("sum is:", nr_1+nr_2)

adunare(1,2)

def nume(nume, prenume):
    print(nume + prenume)

nume("Dumitru", " Daniel")


def print_details(nume, varsta, restanta =0):
    print(f"Hello {nume}, varsta ta este de {varsta} de ani si ai de plata {restanta}")

print_details("Daniel", 30, 270)

def isNumberPrim (number):
    return True

print(isNumberPrim(10))

# ------------------------------------------------------------

def day_of_week(today):
    if today == "sambata" or today == "duminica":
        print("este weekend")
    else: print("Este " + today)

day_of_week("marti")
