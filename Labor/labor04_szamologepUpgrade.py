import labor04_Modul
muvelet = labor04_Modul.muvelet_bekerese()
x = int(labor04_Modul.szam_bekerese())
y = int(labor04_Modul.szam_bekerese())

eredmeny = labor04_Modul.muveletek_vegrehajtasa(muvelet, x, y)

labor04_Modul.eredmenyek_megjelenitese(eredmeny)
