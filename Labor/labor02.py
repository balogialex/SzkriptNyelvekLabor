#szam = 10
'''
szam2 = 20
print(szam)
'''

print("Szia", "due!")
print("Szia due!")
print("szia", "due", sep="-")
print("szia", "\ndue\t!")
print("szia", "due", end='!\n')
print("""Szép napunk 
lesz ma!""")

felhasznalo_neve="Józsi"
felhasznalo_kora= 23
print("----------")
print(felhasznalo_neve)
print("Szia", felhasznalo_neve)
print(f"Neve {felhasznalo_neve}, kora {felhasznalo_kora}")
print("Neve: {0}\nKora: {1}".format(felhasznalo_neve, felhasznalo_kora))

print("------------")
print(felhasznalo_neve.rjust(30,"."))
print(str(felhasznalo_kora).rjust(30,"."))

print(str(felhasznalo_neve).ljust(30,"."))
print(str(felhasznalo_kora).ljust(30,"."))

print(str(felhasznalo_neve).center(30,"."))
print(str(felhasznalo_kora).center(30,"."))

print("-"*10)
felhasznalo_neve = input("Kérem a Nevedet:\t")
felhasznalo_kora = input("Kérem a Korodat:\t")
print(f"\nSzia\t{felhasznalo_neve}")
print(f"Biztosan {felhasznalo_kora} éves vagy? \nNem {int(felhasznalo_kora)+10}?")
