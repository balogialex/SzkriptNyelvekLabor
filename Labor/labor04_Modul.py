
def muvelet_bekerese():
    muvelet = input("Kérek egy műveleti jelet (+,-,*,/)")
    while muvelet not in ("+", "-", "*", "/"):
        print("Nem megfelelő jel\nKérem a másikat")
        muvelet = input("Na akkor melyik leygen?")
    return muvelet

def szam_bekerese():
    x = input("Szám: ")
    while not x.isnumeric():
        x = input("Próbáld meg újra a számot: ")
    return x


def muveletek_vegrehajtasa(muvelet, x, y):
    if muvelet == "+":
        eredmeny = x + y
    elif muvelet == "-":
        eredmeny= x - y
    elif muvelet == "/":
        eredmeny = x / y
    elif muvelet == "*":
        eredmeny = x * y
    return eredmeny

def eredmenyek_megjelenitese(eredmeny):
    print("Művelet eredménye: ", eredmeny)
