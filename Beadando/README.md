# SzkriptNyelvekLabor
Feladat készítője: Balogi Alex (JAU46A)

Feladat leírása:
A program arra szolgál, hogy detektáljon a képernyőn előre megadott képeket és rákattint amikor megtalálta.


Be lehet állítani azt is, hogy mekkora bizonyossággal keressen találatot.
Főbb eseményeket egy szövegdobozba gyűjti (log).

Beépített modulok: tkinter, threading, time, 

Harmadik féltől származó modulok: pyautogui, pillow

Modulok és fügvények felsorolosása: 

main.py: start(), stop(), create_gui(),
BA_ScriptRunner oszály: start_script(), stop_script(), run_script(), log(message)
BA_Modul.py: 
osztály: ba_ImageProcessor: ba_find_and_click_image()