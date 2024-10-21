
print("Jövedelemszámítás")
brutto = int(input("Mennyi a bruttód: "))
eletkor = int(input("Életkorod: "))

if eletkor < 25:
    if brutto > 599790:
        szja=(brutto-599790)*0.15
    else:
        szja=0
else:
    szja = brutto*0.15

nyugdij = brutto*0.15
tb = brutto * 0.07
munkanelkuli = 0.015
netto = brutto -szja-nyugdij-munkanelkuli-tb
print("Jövedelem".center(50))
print("\nSZJA:".ljust(25,"_"), str(szja).rjust(25,"_"), " Ft",sep="")
print("\nNyugdíj járulék:".ljust(25,"_"), str(nyugdij).rjust(25,"_"), " Ft",sep="")
print("\nTársadalom biztosítás".ljust(25,"_"), str(tb).rjust(25,"_"), " Ft",sep="")
print("\nMunkanélküli járulék".ljust(25,"_"), str(munkanelkuli).rjust(25,"_"), " Ft",sep="")
print("\nBruttó jövedelem".ljust(25,"_"), str(brutto).rjust(25,"_"), " Ft",sep="")
print("\nNettó jövedelem".ljust(25,"_"), str(netto).rjust(25,"_"), " Ft",sep="")

