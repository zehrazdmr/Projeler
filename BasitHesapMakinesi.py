import tkinter as kaynak

def topla():
    a=int(sayi1.get())
    b=int(sayi2.get())
    c=a+b
    mesaj_1["text"]=c
def cikar():
    a=int(sayi1.get())
    b=int(sayi2.get())
    c=a-b
    mesaj_1["text"]=c
def carp():
    a=int(sayi1.get())
    b=int(sayi2.get())
    c=a*b
    mesaj_1["text"]=c
def bol():
    a=int(sayi1.get())
    b=int(sayi2.get())
    c=a/b
    mesaj_1["text"]=c

pencere=kaynak.Tk()
pencere.geometry("700x600")
pencere.title("Basit Hesap Makinesi")
pencere.configure(bg="light pink")

yazi_1=kaynak.Label(text="Hoşgeldiniz!",bg="light pink",fg="black",font="helvatica 20 bold")
yazi_1.place(x=150,y=40,width=400,height=80)

topla_buton=kaynak.Button(text="Topla",fg="black",bg="white",font="helvatica 17",command=topla)
topla_buton.place(x=12.5,y=320,width=150,height=80)
cikar_buton=kaynak.Button(text="Çıkar",fg="black",bg="white",font="helvatica 17",command=cikar)
cikar_buton.place(x=187.5,y=320,width=150,height=80)
carp_buton=kaynak.Button(text="Çarpım",fg="black",bg="white",font="helvatica 17",command=carp)
carp_buton.place(x=362.5,y=320,width=150,height=80)
bol_buton=kaynak.Button(text="Bölüm",fg="black",bg="white",font="helvatica 17",command=bol)
bol_buton.place(x=537.5,y=320,width=150,height=80)

sayi1=(kaynak.Entry(bg="white",fg="black",font="verdana 15 bold"))
sayi1.place(x=100,y=100,width=200,height=80)
sayi2=(kaynak.Entry(bg="white",fg="black",font="verdana 15 bold"))
sayi2.place(x=400,y=100,width=200,height=80)

mesaj_1=kaynak.Label(text="Sonuç:",bg="white",fg="black",font="helvatica 20 bold")
mesaj_1.place(x=200,y=200,width=300,height=80)

pencere.mainloop()