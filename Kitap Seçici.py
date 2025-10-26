import turtle
import random
list=["Kürk Mantolu Madonna (Sabahattin Ali)",
"Şeker Portakalı (Jose Mauro De Vasconcelos)",
"1984 (George Orwell)",
"Kırmızı Pazartesi (Gabriel Garcia Marquez)",
"Kuyucaklı Yusuf (Sabahattin Ali)",
"Simyacı (Paulo Coelho)",
"Küçük Prens (Antoine De Saint Exupery)",
"Aklından Bir Sayı Tut (John Verdon)",
"Yabancı (Albert Camus)",
"Saatleri Ayarlama Enstitüsü (Ahmet Hamdi Tanpınar)",
"Aşkın Gözyaşları (Sinan Yağmur)",
"Nar Ağacı (Nazan Bekiroğlu)",
"Tutunamayanlar (Oğuz Atay)",
"Aylak Adam (Yusuf Atılgan)",
"Sol Ayağım (Christy Brown)",
"Sevda Sözleri (Cemal Süreya)",
"Zeytindağı (Falih Rıfkı Atay)",
"Semerkant (Amin Maalouf)",
"Bülbülü Öldürmek (Harper Lee)",
"Bir Ömür Nasıl Yaşanır? (İlber Ortaylı)",
"Osmanlı Tarihinde Efsaneler ve Gerçekler (Halil İnalcık)"]
pencere=turtle.Screen()
pencere.title("Bir Sonraki kitabımızı seçelim")
pencere.bgcolor('#5a5acd')

çerçeve=turtle.Turtle()
çerçeve.color('white')
çerçeve.setx(-255)
çerçeve.sety(-250)
çerçeve.pen(pensize=5)
for i in range(4):
    çerçeve.forward(500)
    çerçeve.left(90)
    çerçeve.reset()
yaz=turtle.Turtle()
yaz.color('#a0ffff')
yaz.setx(-250)
yaz.write("{}".format(random.choice(list)),font=("Helvatica", 18, "normal"))

çerçeve.hideturtle()
yaz.hideturtle()
pencere.exitonclick()




