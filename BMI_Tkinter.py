import tkinter

window=tkinter.Tk()
window.title("BMI")
window.minsize(450,300)

def gettinginformation():
    global sonuc_label
    global kullanici_boy
    global kullanici_kilo

    kullanici_boy=boy_entry.get()
    kullanici_kilo=kilo_entry.get()

    try:



        boy1=int(kullanici_boy)/100

        boy2=boy1**2
        sonuc=int(kullanici_kilo)/boy2
        sonuc1=str(sonuc)
        sonuc=sonuc1[0:5:1]
        sonuc1=float(sonuc)
        durum_list=["Zayıf","Normal","Kilolu","Obez"]
        if (sonuc1 < 18.50):
            global durum
            durum=durum_list[0]

        elif(18.5<sonuc1<24.99):
            durum=durum_list[1]
        elif(25<sonuc1<29.99):
            durum=durum_list[2]
        elif(30<sonuc1):
            durum=durum_list[3]


        sonuc1=str(sonuc1)
        sonuc_label.config(text="Vücut kitle indeksiniz {} bu durumda siz {} bir insansınız".format(sonuc1[0:5:1],durum))



    except:

        sonuc_label.config(text="Lütfen girdiğiniz değerleri kontrol edin")
#button

sistem_button=tkinter.Button(text="Sonuçlandır",command=gettinginformation)




#label

sistemb_label=tkinter.Label(text="Boyunuzu giriniz(cm)")

sistemk_label=tkinter.Label(text="Kilonuzu giriniz(kg)")
#entry

boy_entry=tkinter.Entry()

kilo_entry=tkinter.Entry()



sistemb_label.pack()
boy_entry.pack()
sistemk_label.pack()
kilo_entry.pack()
sistem_button.pack()
sonuc_label = tkinter.Label(text="")
sonuc_label.pack()

window.mainloop()

