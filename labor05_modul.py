def felhasznalonev():
    _felhasznalo_neve = input("Kérem a felhasználói nevét! (E-Mail)")
    while " " in _felhasznalo_neve or not "@" in _felhasznalo_neve or not "." in _felhasznalo_neve:
        print("Érvénytelen email formátum!")
        if " " in _felhasznalo_neve:
            print("Szőköz van email-ben!")
        if "@" not in _felhasznalo_neve:
            print("Nincs kukac")
        if "." not in _felhasznalo_neve:
            print("Nincs pont")
        _felhasznalo_neve = input("Kérem a felhasználói nevét! (E-Mail)")
    print("OK!")
    return _felhasznalo_neve

def jelszo_bekerese():

    def jelszo_hossza(_jelszo, _hossz):
        ok = True
        if len(_jelszo) < _hossz:
            ok = False
        return ok

    def szamjegy(_jelszo):
        ok = False
        for betu in _jelszo:
            if betu.isnumeric():
                ok = True
                break
        return ok

    def nagybetu(_jelszo):
        ok = False
        for betu in _jelszo:
            if betu.isupper():
                ok = True
                break
        return ok

    def kisbetu(_jelszo):
        ok = False
        for betu in _jelszo:
            if betu.islower():
                ok = True
                break
        return ok

    jelszo = input("Kérek egy jelszot! ")
    while not  jelszo_hossza(jelszo, 10) or not szamjegy(jelszo) or not kisbetu(jelszo) or not nagybetu(jelszo):
        print("Rossz jelszó formátum!\n")
        jelszo = input("Kérek egy jelszot! ")
    return jelszo