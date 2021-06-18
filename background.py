class Produkti:
  emri = ""
  pesha = 0
  njesia_matese = ""
  cmimi = 0
  zbritja = 0
  sasia = 0

  def __init__(self, _emri, _pesha, _njesia_matese, _cmimi,  _zbritja, _sasia):
      self.emri = _emri
      self.pesha = _pesha
      self.njesia_matese = _njesia_matese
      self.cmimi = _cmimi
      self.zbritja = _zbritja
      self.sasia = _sasia

  def pagesaPerPije(self):
    #variabla per llogaritjen e zbritjes per produktin e trete 
    zbritjaProduktiTrete = self.cmimi - (self.cmimi * (self.zbritja / 100))
    if(self.sasia < 3):
      return(self.sasia * self.cmimi)
    #P.sh per 3 produkte qe kushtojne nga 2 euro, produkti i trete llogaritet me nje perqindje te zbritur ne cmim dhe jo falas
    #(Kerkesa nr.3 ne detyre)
    elif(self.sasia == 3):
      return((self.cmimi * 2) + zbritjaProduktiTrete)  
    #Nese sasia eshte me e madhe se 3, 3 produkte llogariten me oferte, kurse te tjerat llogariten me cmimin e nje produkti vec e vec
    #Ky kusht vlen vetem per produktet qe kur modulohen me 3, nuk japin rezultatin 0. P.sh 5 produkte
    #(Kerkesa nr.1 ne detyre)
    elif(self.sasia > 3 and self.sasia % 3 != 0):
      return((self.cmimi * 2) + zbritjaProduktiTrete + ((self.sasia - 3)) * self.cmimi)  
    #nese produktet perfshihen ne oferte, psh 6 produkte, 9 produkte
    elif(self.sasia % 3 == 0):
      return(((self.cmimi * 2) + zbritjaProduktiTrete)*(self.sasia/3)) 
    
  def pagesaPijePaOferte(self):
      return(self.sasia * self.cmimi)

  def pagesaPerFruta(self):
    #Sasia e dhene nga perdoruesi shumezohet me cmimin per kilogram
    #Kerkesa nr.2 e detyres
    return(self.sasia * self.cmimi)

#objektet e produkteve     
molla = Produkti("Molla", 1,"kg", 1.50, 0, 0)
dardha = Produkti("Dardha", 1, "kg", 2.00, 0, 0)
kumbulla = Produkti("Kumbulla", 1, "kg", 1.30, 0, 0)
qershi = Produkti("Qershi", 1, "kg", 1.70, 0, 0)
pjeshka = Produkti("Pjeshka", 1, "kg", 1.20, 0, 0)
fanta = Produkti("Fanta", 2, "l", 1.80, 20, 0)
cocacola = Produkti("Coca-Cola", 2, "l", 1.50, 40, 0)
sprite = Produkti ("Sprite", 1.5, "l", 1.30, 30, 0)
aloevera = Produkti ("Aloe Vera", 1.5, "l", 1.10, 30, 0)
icetea = Produkti ("Ice Tea", 1.5, "l", 1.40, 30, 0)


pijetMeOferte = [fanta, cocacola, aloevera]
pijetPaOferte = [sprite, icetea]
frutat = [molla, dardha, kumbulla, qershi, pjeshka]

def background():
    import random,turtle,time
    from turtle import Screen
    screen = turtle.Screen()
    screen.setup(width = 1.0, height = 1.0)
    window = turtle.Screen()
    window.bgpic('shopping.png')
    
    turtle.hideturtle()
    turtle.color("black")
    turtle.penup()
    turtle.setposition(-300, 245)
    style = ("Arial",26,"bold")
    turtle.write("MENYJA E PRODUKTEVE NË DYQAN", font=style)
    turtle.pendown()
    turtle.penup()
    turtle.hideturtle()
    turtle.color("DarkGoldenrod1")
    turtle.setposition(-370, 210)
    style = ("Arial",22)
    turtle.write("FRUTAT", font=style)
    turtle.pendown()
    #produkti,pesha,cmimi
    produkti_emri = turtle.Turtle()
    produkti_emri.speed(0.1)
    produkti_emri.color("white", "lightgreen")
    produkti_emri.hideturtle()
    produkti_emri.penup()
    produkti_emri.setpos(-500, 160)
    produkti_emri.pendown()
    produkti_emri.begin_fill()

    for i in range(2):
        produkti_emri.forward(400)
        produkti_emri.left(90)
        produkti_emri.forward(50)
        produkti_emri.left(90)
        
    produkti_emri.end_fill()
    produkti_emri.penup()

    produkti_emri.setposition(-506, 165)
    style = ("Arial",25)
    produkti_emri.color("DarkSeaGreen4")
    produkti_emri.write("   Produkti - Pesha - Cmimi",font=style)
    produkti_emri.pendown()

    #molla
    produktimolla = turtle.Turtle()
    produktimolla.speed(0.1)
    produktimolla.color("white", "lightgreen")
    produktimolla.hideturtle()
    produktimolla.penup()
    produktimolla.setpos(-500, 80)
    produktimolla.pendown()
    produktimolla.begin_fill()

    for i in range(2):
        produktimolla.forward(400)
        produktimolla.left(90)
        produktimolla.forward(50)
        produktimolla.left(90)
        
    produktimolla.end_fill()
    produktimolla.penup()

    produktimolla.setposition(-480, 85)
    style = ("Arial",25,"bold")
    #variablatmolla = (molla.emri, molla.pesha, molla.njesia_matese, molla.cmimi, "€")
    produktimolla.write(molla.emri,font=style)
    produktimolla.setposition(-320, 85)
    produktimolla.write(molla.pesha,font=style)
    produktimolla.setposition(-300, 85)
    produktimolla.write(molla.njesia_matese,font=style)
    produktimolla.setposition(-190, 85)
    produktimolla.write(molla.cmimi, font=style)
    produktimolla.setposition(-140, 85)
    produktimolla.write("€", font=style)
    produktimolla.pendown()

    #dardha
    produktidardha = turtle.Turtle()
    produktidardha.speed(0.1)
    produktidardha.color("white", "lightgreen")
    produktidardha.hideturtle()
    produktidardha.penup()
    produktidardha.setpos(-500, 0)
    produktidardha.pendown()
    produktidardha.begin_fill()

    for i in range(2):
        produktidardha.forward(400)
        produktidardha.left(90)
        produktidardha.forward(50)
        produktidardha.left(90)
        

    produktidardha.end_fill()
    produktidardha.penup()

    produktidardha.setposition(-480, 5)
    produktidardha.write(dardha.emri,font=style)
    produktidardha.setposition(-320, 5)
    produktidardha.write(dardha.pesha,font=style)
    produktidardha.setposition(-300, 5)
    produktidardha.write(dardha.njesia_matese,font=style)
    produktidardha.setposition(-190, 5)
    produktidardha.write(dardha.cmimi, font=style)
    produktidardha.setposition(-140, 5)
    produktidardha.write("€", font=style)
    produktidardha.pendown()

    #kumbulla
    produktikumbulla = turtle.Turtle()
    produktikumbulla.speed(0.1)
    produktikumbulla.color("white", "lightgreen")
    produktikumbulla.hideturtle()
    produktikumbulla.penup()
    produktikumbulla.setpos(-500, -80)
    produktikumbulla.pendown()
    produktikumbulla.begin_fill()

    for i in range(2):
        produktikumbulla.forward(400)
        produktikumbulla.left(90)
        produktikumbulla.forward(50)
        produktikumbulla.left(90)
        

    produktikumbulla.end_fill()
    produktikumbulla.penup()

    produktikumbulla.setposition(-480, -75)
    produktikumbulla.write(kumbulla.emri,font=style)
    produktikumbulla.setposition(-320, -75)
    produktikumbulla.write(kumbulla.pesha,font=style)
    produktikumbulla.setposition(-300, -75)
    produktikumbulla.write(kumbulla.njesia_matese,font=style)
    produktikumbulla.setposition(-190, -75)
    produktikumbulla.write(kumbulla.cmimi, font=style)
    produktikumbulla.setposition(-140, -75)
    produktikumbulla.write("€", font=style)
    produktikumbulla.pendown()

    #qershi
    produktiqershi = turtle.Turtle()
    produktiqershi.speed(0.1)
    produktiqershi.color("white", "lightgreen")
    produktiqershi.hideturtle()
    produktiqershi.penup()
    produktiqershi.setpos(-500, -160)
    produktiqershi.pendown()
    produktiqershi.begin_fill()

    for i in range(2):
        produktiqershi.forward(400)
        produktiqershi.left(90)
        produktiqershi.forward(50)
        produktiqershi.left(90)
        
    produktiqershi.end_fill()
    produktiqershi.penup()

    produktiqershi.setposition(-480, -155)
    produktiqershi.write(qershi.emri,font=style)
    produktiqershi.setposition(-320, -155)
    produktiqershi.write(qershi.pesha,font=style)
    produktiqershi.setposition(-300, -155)
    produktiqershi.write(qershi.njesia_matese,font=style)
    produktiqershi.setposition(-190, -155)
    produktiqershi.write(qershi.cmimi, font=style)
    produktiqershi.setposition(-140, -155)
    produktiqershi.write("€", font=style)
    produktiqershi.pendown()

    #pjeshka
    produktipjeshka = turtle.Turtle()
    produktipjeshka.speed(0.1)
    produktipjeshka.color("white", "lightgreen")
    produktipjeshka.hideturtle()
    produktipjeshka.penup()
    produktipjeshka.setpos(-500, -240)
    produktipjeshka.pendown()
    produktipjeshka.begin_fill()

    for i in range(2):
        produktipjeshka.forward(400)
        produktipjeshka.left(90)
        produktipjeshka.forward(50)
        produktipjeshka.left(90)
        
    produktipjeshka.end_fill()
    produktipjeshka.penup()

    produktipjeshka.setposition(-480, -235)
    produktipjeshka.write(pjeshka.emri,font=style)
    produktipjeshka.setposition(-320, -235)
    produktipjeshka.write(pjeshka.pesha,font=style)
    produktipjeshka.setposition(-300, -235)
    produktipjeshka.write(pjeshka.njesia_matese,font=style)
    produktipjeshka.setposition(-190, -235)
    produktipjeshka.write(pjeshka.cmimi, font=style)
    produktipjeshka.setposition(-140, -235)
    produktipjeshka.write("€", font=style)
    produktipjeshka.pendown()
    turtle.penup()
    turtle.hideturtle()
    turtle.color("DarkGoldenrod1")
    turtle.setposition(260, 210)
    style = ("Arial",22)
    turtle.write("PIJET", font=style)
    turtle.pendown()


    #produkti,pesha,cmimi
    produkti2_emri = turtle.Turtle()
    produkti2_emri.speed(0.1)
    produkti2_emri.color("white", "lightgreen")
    produkti2_emri.hideturtle()
    produkti2_emri.penup()
    produkti2_emri.setpos(95, 160)
    produkti2_emri.pendown()
    produkti2_emri.begin_fill()

    for i in range(2):
        produkti2_emri.forward(400)
        produkti2_emri.left(90)
        produkti2_emri.forward(50)
        produkti2_emri.left(90)
        
    produkti2_emri.end_fill()
    produkti2_emri.penup()

    produkti2_emri.setposition(85, 165)
    style = ("Arial",25)
    produkti2_emri.color("DarkSeaGreen4")
    produkti2_emri.write("   Produkti - Pesha - Cmimi",font=style)
    produkti2_emri.pendown()

    #fanta
    produktifanta = turtle.Turtle()
    produktifanta.speed(0.1)
    produktifanta.color("white", "lightgreen")
    produktifanta.hideturtle()
    produktifanta.penup()
    produktifanta.setpos(95, 80)
    produktifanta.pendown()
    produktifanta.begin_fill()

    for i in range(2):
        produktifanta.forward(400)
        produktifanta.left(90)
        produktifanta.forward(50)
        produktifanta.left(90)
        
    produktifanta.end_fill()
    produktifanta.penup()

    produktifanta.setposition(110, 85)
    style = ("Arial",25,"bold")
    produktifanta.write(fanta.emri,font=style)
    produktifanta.setposition(300, 85)
    produktifanta.write(fanta.pesha,font=style)
    produktifanta.setposition(320, 85)
    produktifanta.write(fanta.njesia_matese,font=style)
    produktifanta.setposition(410, 85)
    produktifanta.write(fanta.cmimi, font=style)
    produktifanta.setposition(460, 85)
    produktifanta.write("€", font=style)
    produktifanta.pendown()

    #cocacola
    produkticocacola = turtle.Turtle()
    produkticocacola.speed(0.1)
    produkticocacola.color("white", "lightgreen")
    produkticocacola.hideturtle()
    produkticocacola.penup()
    produkticocacola.setpos(95, 0)
    produkticocacola.pendown()
    produkticocacola.begin_fill()

    for i in range(2):
        produkticocacola.forward(400)
        produkticocacola.left(90)
        produkticocacola.forward(50)
        produkticocacola.left(90)
        
    produkticocacola.end_fill()
    produkticocacola.penup()

    produkticocacola.setposition(110, 5)
    produkticocacola.write(cocacola.emri,font=style)
    produkticocacola.setposition(300, 5)
    produkticocacola.write(cocacola.pesha,font=style)
    produkticocacola.setposition(320, 5)
    produkticocacola.write(cocacola.njesia_matese,font=style)
    produkticocacola.setposition(410, 5)
    produkticocacola.write(cocacola.cmimi, font=style)
    produkticocacola.setposition(460, 5)
    produkticocacola.write("€", font=style)
    produkticocacola.pendown()

    #Sprite
    produktisprite = turtle.Turtle()
    produktisprite.speed(0.1)
    produktisprite.color("white", "lightgreen")
    produktisprite.hideturtle()
    produktisprite.penup()
    produktisprite.setpos(95, -80)
    produktisprite.pendown()
    produktisprite.begin_fill()

    for i in range(2):
        produktisprite.forward(400)
        produktisprite.left(90)
        produktisprite.forward(50)
        produktisprite.left(90)
        
    produktisprite.end_fill()
    produktisprite.penup()

    produktisprite.setposition(110, -75)
    produktisprite.write(sprite.emri,font=style)
    produktisprite.setposition(290, -75)
    produktisprite.write(sprite.pesha,font=style)
    produktisprite.setposition(340, -75)
    produktisprite.write(sprite.njesia_matese,font=style)
    produktisprite.setposition(410, -75)
    produktisprite.write(sprite.cmimi, font=style)
    produktisprite.setposition(460, -75)
    produktisprite.write("€", font=style)
    produktisprite.pendown()

    #aloevera
    produktialoevera = turtle.Turtle()
    produktialoevera.speed(0.1)
    produktialoevera.color("white", "lightgreen")
    produktialoevera.hideturtle()
    produktialoevera.penup()
    produktialoevera.setpos(95, -160)
    produktialoevera.pendown()
    produktialoevera.begin_fill()

    for i in range(2):
        produktialoevera.forward(400)
        produktialoevera.left(90)
        produktialoevera.forward(50)
        produktialoevera.left(90)
        
    produktialoevera.end_fill()
    produktialoevera.penup()

    produktialoevera.setposition(110, -155)
    produktialoevera.write(aloevera.emri,font=style)
    produktialoevera.setposition(290, -155)
    produktialoevera.write(aloevera.pesha,font=style)
    produktialoevera.setposition(340, -155)
    produktialoevera.write(aloevera.njesia_matese,font=style)
    produktialoevera.setposition(410, -155)
    produktialoevera.write(aloevera.cmimi, font=style)
    produktialoevera.setposition(460, -155)
    produktialoevera.write("€", font=style)
    produktialoevera.pendown()

    #icetea
    produktiicetea = turtle.Turtle()
    produktiicetea.speed(0.1)
    produktiicetea.color("white", "lightgreen")
    produktiicetea.hideturtle()
    produktiicetea.penup()
    produktiicetea.setpos(95, -240)
    produktiicetea.pendown()
    produktiicetea.begin_fill()

    for i in range(2):
        produktiicetea.forward(400)
        produktiicetea.left(90)
        produktiicetea.forward(50)
        produktiicetea.left(90)
        
    produktiicetea.end_fill()
    produktiicetea.penup()

    produktiicetea.setposition(110, -235)
    produktiicetea.write(icetea.emri,font=style)
    produktiicetea.setposition(290, -230)
    produktiicetea.write(icetea.pesha,font=style)
    produktiicetea.setposition(340, -230)
    produktiicetea.write(icetea.njesia_matese,font=style)
    produktiicetea.setposition(410, -230)
    produktiicetea.write(icetea.cmimi, font=style)
    produktiicetea.setposition(460, -230)
    produktiicetea.write("€", font=style)
    produktiicetea.pendown()

    #blej
    blej = turtle.Turtle()
    blej.speed(0.1)
    blej.color("brown", "DarkGoldenrod1")
    blej.hideturtle()
    blej.penup()
    blej.setpos(-60, -300)
    blej.pendown()
    blej.fillcolor("DarkGoldenrod1")
    blej.begin_fill()

    for i in range(2):
        blej.forward(120)
        blej.left(90)
        blej.forward(50)
        blej.left(90)
        
    blej.end_fill()
    blej.penup()

    blej.setposition(-45, -300)
    style = ("Arial",28,"bold")
    blej.write("BLEJ", font=style)
    blej.pendown()

    


    
