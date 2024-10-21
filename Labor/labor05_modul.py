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
    return _felhasznalo_neve
def jelszo_ellenorzese(jelszo):
    ok = True
    probalkozasok = 0
    while True:
        jelszo2 = input("Kérema  jelszót ismét: ")
        if jelszo2 == jelszo:
            break
        else:
            print("Nem azonos a jelszó! Próbálja újra!")
            probalkozasok+=1
            if probalkozasok == 3:
                ok = False
                break
    return ok
def regisztracio():

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
        while not  jelszo_hossza(jelszo, 8) or not szamjegy(jelszo) or not kisbetu(jelszo) or not nagybetu(jelszo):
            print("Rossz jelszó formátum!\n")
            jelszo = input("Kérek egy jelszot! ")
        return jelszo

    def rogzites(email, jelszo):
        with open('dolgozok.txt', 'a', encoding='utf-8') as fajl:
            fajl.write(email + ";" + jelszo + "\n")

    felhasznalo_neve = felhasznalonev()
    felhasznalo_jelszava = jelszo_bekerese()
    ok = jelszo_ellenorzese(felhasznalo_jelszava)
    if ok:
        rogzites(felhasznalo_neve, felhasznalo_jelszava)
    return ok
def beleptetes():
    def felhasznalo_bekerese():
        jelszo = False
        email = felhasznalonev()
        with open('dolgozok.txt', 'r', encoding='utf-8') as fajl:
            for sor in fajl:
                felhasznalo = sor.strip().split(";")
                if felhasznalo[0] == email:
                    jelszo = felhasznalo[1]
                    break
        return jelszo

    felhasznalo = felhasznalo_bekerese()
    if not felhasznalo:
        print("Nincs ilyen felhasználó!")
    else:
        if jelszo_ellenorzese(felhasznalo):
            print("Sikerült belépned!")
        else:
            print("Belépés megtagadva")