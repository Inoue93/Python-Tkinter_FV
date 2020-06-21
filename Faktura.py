import tkinter
import time
import tkinter.messagebox
from tkinter import ttk
from time import strftime

okno = tkinter.Tk() #Otwieranie okna
okno.minsize(650,500)
okno.title("Paragon")

now = time.strftime("%Y-%m-%d_%H-%M")
plik = open("file " + str(now) + ".txt", 'w+')

listatowarow = []
koszty = 0
rVal = tkinter.IntVar()


def clickDodaj(): #Definiowanie działania przycisku po kliknięciu
    tkinter.messagebox.showinfo("","Dodano")

    towary_firmy = etowar.get()
    towary_firmy2 = etowar2.get()
    towary_firmy3 = etowar3.get()
    towary_firmy4 = etowar4.get()


    sumatowarow = towary_firmy + towary_firmy2, towary_firmy3, towary_firmy4
    listatowarow.append(sumatowarow)
    print(listatowarow)

    if towary_firmy3 == "23%":
        procent = 1.23 * float(towary_firmy4)
    elif towary_firmy3 == "8%":
        procent = 1.08 * float(towary_firmy4)
    elif towary_firmy3 == "3%":
        procent = 1.03 * float(towary_firmy4)
    else:
        procent = float(towary_firmy4)

    print(procent)
    global koszty
    koszty += procent
    print(koszty)

    etowar.delete(0,tkinter.END)
    etowar2.delete(0,tkinter.END)
    etowar3.delete(0,tkinter.END)
    etowar4.delete(0,tkinter.END)



def clickZakończ():
    okno3 = tkinter.Tk()
    okno3.minsize(200, 200)
    okno3.title("Płatność")


    suma1 = tkinter.Label(okno3, text="Do zapłaty: ")
    esuma = tkinter.Text(okno3, width=10, height=1)
    esuma.insert(tkinter.END, koszty)
    rodzaj= tkinter.Label(okno3, text="Rodzaj płatności: ")
    R1 = tkinter.Radiobutton(okno3, text='Karta', variable=rVal, value=10)
    R2 = tkinter.Radiobutton(okno3, text='Gotówka', variable=rVal, value=50)

    platnosc = tkinter.Label(okno3, text="Zapłacona kwota: ")
    eplatnosc = tkinter.Spinbox(okno3, from_=0, to=100, width=10)


    zaplata = eplatnosc.get()
    ereszta = float(zaplata) - koszty


    reszta = tkinter.Label(okno3, text="Reszta wynosi ")
    reszta2 = tkinter.Text(okno3, width=10, height=1)
    reszta2.insert(tkinter.END, ereszta)

    wydruk = tkinter.Button(okno3, text='Zakończ paragon', command=clickWydrukParagonu())

    suma1.grid(row=0, column=0, sticky=tkinter.W)
    esuma.grid(row=0, column=1, sticky=tkinter.W)
    rodzaj.grid(row=1, column=0, sticky=tkinter.W)
    R1.grid(row=2, column=0, sticky=tkinter.W)
    R2.grid(row=2, column=1, sticky=tkinter.W)
    platnosc.grid(row=3, column=0, sticky=tkinter.W)
    eplatnosc.grid(row=3, column=1, sticky=tkinter.W)
    reszta.grid(row=4, column=0, sticky=tkinter.W)
    reszta2.grid(row=4, column=1, sticky=tkinter.W)
    wydruk.grid(row=6, column=1, sticky=tkinter.W)

def clickWydrukParagonu():
    firma = enazwafirmy.get()
    firma_adres = eadresfirmy.get()
    firma_adres2 = eadresfirmy2.get()
    firma_adres3 = eadresfirmy3.get()
    firma_adres4 = eadresfirmy4.get()
    sklep_nazwa = enazwasklepu.get()
    nipy = enip.get()
    nipy2 = enip2.get()
    nipy3 = enip3.get()
    nipy4 = enip4.get()
    towary_firmy = etowar.get()
    towary_firmy2 = etowar2.get()
    towary_firmy3 = etowar3.get()
    towary_firmy4 = etowar4.get()
    rodzaj_platnosci = rVal.get()
    #zaplata = eplatnosc.get()
    #reszta1 = ereszta.get()


    plik.write("Nazwa firmy: ")
    plik.write(firma)
    plik.write("\n")
    plik.write("Kod pocztowy: ")
    plik.write(firma_adres)
    plik.write("-")
    plik.write(firma_adres2)
    plik.write("\n")
    plik.write("Miasto: ")
    plik.write(firma_adres3)
    plik.write("\n")
    plik.write("Ulica: ")
    plik.write(firma_adres4)
    plik.write("\n")
    plik.write("Nazwa sklepu: ")
    plik.write(sklep_nazwa)
    plik.write("\n")
    plik.write("Numer NIP: ")
    plik.write(nipy)
    plik.write("-")
    plik.write(nipy2)
    plik.write("-")
    plik.write(nipy3)
    plik.write("-")
    plik.write(nipy4)
    plik.write("\n")
    plik.write("\n")
    plik.write("Lista towarów: ")
    # plik.write(listatowarow)
    plik.write("\n")
    plik.write("\n")
    plik.write("Kwota do zapłaty: ")
    # plik.write(koszty)
    plik.write("\n")
    if rVal == 10:
        plik.write("Sposób płatności: Karta")
    elif rVal == 50:
        plik.write("Sposób płatności: Gotówka")
    plik.write("\n")
    plik.write("Zapłacono: ")
    #plik.write(zaplata)
    plik.write("\n")
    plik.write("Reszta: ")
    #plik.write(reszta1)



    plik.close()


nazwafirmy = tkinter.Label(okno,text="Nazwa firmy: ")
adresfirmy = tkinter.Label(okno,text="Kod pocztowy: ")
adresfirmy2 = tkinter.Label(okno,text="Misto ")
adresfirmy3 = tkinter.Label(okno,text="Ulica: ")
nazwasklepu = tkinter.Label(okno,text="Nazwa sklepu: ")
nip = tkinter.Label(okno,text="Numer NIP: ")
data = tkinter.Label(okno,text="Data: ")
towary = tkinter.Label(okno,text="Towary: ", bd=2)
towary2 = tkinter.Label(okno,text="Nazwa produktu:")
towary3 = tkinter.Label(okno,text="Ilość")
towary4 = tkinter.Label(okno,text="VAT")
towary5 = tkinter.Label(okno,text="Cena jednostkowa:")


dodaj = tkinter.Button(okno, fg="red", text = 'Dodaj towar', command = clickDodaj)
zakończ = tkinter.Button(okno, text = 'Podsumowanie', command = clickZakończ)

enazwafirmy = tkinter.Entry(okno)
eadresfirmy = tkinter.Entry(okno, width = 10)
eadresfirmy2 = tkinter.Entry(okno, width = 15)
eadresfirmy3 = tkinter.Entry(okno)
eadresfirmy4 = tkinter.Entry(okno)
enazwasklepu = tkinter.Entry(okno)
enip = tkinter.Entry(okno, width=15)
enip2 = tkinter.Entry(okno, width=15)
enip3 = tkinter.Entry(okno, width=10)
enip4 = tkinter.Entry(okno, width=10)
edata =  tkinter.Text(okno, width=10, height=1)
edata.insert(tkinter.END, now)
etowar =  tkinter.Entry(okno)
etowar2 = tkinter.Spinbox(okno, from_=1, to=100, width=10)
etowar3 = ttk.Combobox(okno, values=[
                                    "23%",
                                    "8%",
                                    "3%",
                                    "zw"], width = 5)

etowar4 = tkinter.Entry(okno, width=10)



nazwafirmy.grid(row = 0, column = 0, sticky=tkinter.W)
adresfirmy.grid(row = 1, column = 0, sticky=tkinter.W)
adresfirmy2.grid(row = 2, column = 0, sticky=tkinter.W)
adresfirmy3.grid(row = 3, column = 0, sticky=tkinter.W)
nazwasklepu.grid(row = 4, column = 0, sticky=tkinter.W)
nip.grid(row = 5, column = 0, sticky=tkinter.W)
data.grid(row = 6, column = 0, sticky=tkinter.W)
towary.grid(row = 8, column = 0, sticky=tkinter.W)
towary2.grid(row = 8, column = 1, sticky=tkinter.W)
towary3.grid(row = 8, column = 2, sticky=tkinter.W)
towary4.grid(row = 8, column = 3, sticky=tkinter.W)
towary5.grid(row = 8, column = 4, sticky=tkinter.W)

dodaj.grid(row=10, column = 5)
zakończ.grid(row=13, column = 3)
#karta.grid(row=16, column = 0)
#gotówka.grid(row=16, column = 1)

enazwafirmy.grid(row=0, column = 1)
eadresfirmy.grid(row=1, column = 1)
eadresfirmy2.grid(row=1, column = 2)
eadresfirmy3.grid(row=2, column = 1)
eadresfirmy4.grid(row=3, column = 1)
enazwasklepu.grid(row=4, column = 1)
enip.grid(row=5, column = 1)
enip2.grid(row=5, column = 2)
enip3.grid(row=5, column = 3)
enip4.grid(row=5, column = 4)
edata.grid(row=6, column = 1)
etowar.grid(row=9, column = 1)
etowar2.grid(row=9, column = 2)
etowar3.grid(row=9, column = 3)
etowar4.grid(row=9, column = 4)
#esuma11.grid(row=11, column = 1)





okno.mainloop() #Pętla dla okna

