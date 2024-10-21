from turtledemo.paint import switchupdown

muvelet= input("Kérek egy műveleti jelet (+,-,*,/)")
if muvelet in ("+","-","*","/"):
    x=int(input("Elsőszám: "))
    y=int(input("Másodikszám: "))
    if muvelet == "+":
        print("Összeadás eredménye: ", x+y)
    elif muvelet == "-":
        print("Kivonás eredménye: ", x-y)
    elif muvelet == "/":
        print("Osztás eredménye: ", x/y)

else:
    print("Nem megfelelő jel")
    exit()
