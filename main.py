class Produkti:
  emri = ""
  pesha = 0
  njesia_matese = ""
  cmimi = 0
  zbritja = 0

  def __init__(self, _emri, _pesha, _njesia_matese, _cmimi,  _zbritja):
      self.emri = _emri
      self.pesha = _pesha
      self.njesia_matese = _njesia_matese
      self.cmimi = _cmimi
      self.zbritja = _zbritja

  def pagesaPerPije(self):
    #variabla per llogaritjen e zbritjes per produktin e trete 
    zbritjaProduktiTrete = self.cmimi - (self.cmimi * (self.zbritja / 100))
    if(sasia < 3):
      return(sasia * self.cmimi)
    #P.sh per 3 produkte qe kushtojne nga 2 euro, produkti i trete llogaritet me nje perqindje te zbritur ne cmim dhe jo falas
    #(Kerkesa nr.3 ne detyre)
    elif(sasia == 3):
      return((self.cmimi * 2) + zbritjaProduktiTrete)  
    #Nese sasia eshte me e madhe se 3, 3 produkte llogariten me oferte, kurse te tjerat llogariten me cmimin e nje produkti vec e vec
    #Ky kusht vlen vetem per produktet qe kur modulohen me 3, nuk japin rezultatin 0. P.sh 5 produkte
    #(Kerkesa nr.1 ne detyre)
    elif(sasia > 3 and sasia % 3 != 0):
      return((self.cmimi * 2) + zbritjaProduktiTrete + ((sasia - 3)) * self.cmimi)  
    #nese produktet perfshihen ne oferte, psh 6 produkte, 9 produkte
    elif(sasia % 3 == 0):
      return(sasia*self.cmimi - (sasia/2* zbritjaProduktiTrete))
    
  def pagesaPijePaOferte(self):
      return(sasia * self.cmimi)

  def pagesaPerFruta(self):
    #Sasia e dhene nga perdoruesi shumezohet me cmimin per kilogram
    #Kerkesa nr.2 e detyres
    return(sasia * self.cmimi)

#objektet e produkteve     
molla = Produkti("Molla", 1,"kg", 1.50, 0)
dardha = Produkti("Dardha", 1, "kg", 2.00, 0)
kumbulla = Produkti("Kumbulla", 1, "kg", 1.50, 0)
qershi = Produkti("Qershi", 1, "kg", 1.50, 0)
pjeshka = Produkti("Pjeshka", 1, "kg", 1.50, 0)
fanta = Produkti("Fanta", 2, "l", 2.00, 20)
cocacola = Produkti("Coca-Cola", 2, "l", 1.50, 40)
vishnje = Produkti ("Vishnje", 1.5, "l", 1.30,30)

print("Menyja e produkteve ne dyqan:")
print("Produkti: Pesha: Njesia matese:  Cmimi:")  
print(molla.emri, molla.pesha, molla.njesia_matese, molla.cmimi, "€")
print(dardha.emri, dardha.pesha, dardha.njesia_matese, dardha.cmimi, "€")
print(kumbulla.emri, kumbulla.pesha, kumbulla.njesia_matese, kumbulla.cmimi, "€")
print(qershi.emri, qershi.pesha, qershi.njesia_matese, qershi.cmimi, "€")
print(pjeshka.emri, pjeshka.pesha, pjeshka.njesia_matese, pjeshka.cmimi, "€")
print(fanta.emri, fanta.pesha, fanta.njesia_matese, fanta.cmimi, "€")
print(cocacola.emri, cocacola.pesha, cocacola.njesia_matese, cocacola.cmimi, "€")
print(vishnje.emri, vishnje.pesha, vishnje.njesia_matese, vishnje.cmimi, "€")

pijetMeOferte = [fanta, cocacola]
pijetPaOferte = [vishnje]
frutat = [molla, dardha, kumbulla, qershi, pjeshka]

produkt = eval(input("Ju lutem shkruani produktin qe deshironi te blini! "))
if produkt.njesia_matese == 'kg':
  sasia = float(input("Ju lutem shkruani sasine ne kilogram! (P.sh 0.30"))
else:
  sasia = int(input("Ju lutem shkruani sasine ne cope! "))
  
def main():
  pagesa_totale = 0
  # Variabla per te ju pergjigjur programit
  pyetja = ('po', 'jo', 'ndalu')
  global produkt
  
  if produkt in pijetMeOferte:
    pagesaeProduktit = produkt.pagesaPerPije()
    print("Cmimi eshte: ", pagesaeProduktit, " euro")
  elif produkt in pijetPaOferte:
    pagesaeProduktit = produkt.pagesaPijePaOferte()
    print("Cmimi eshte: ", pagesaeProduktit, " euro")
  elif produkt in frutat:
    pagesaeProduktit = produkt.pagesaPerFruta()
    print("Cmimi eshte: ", pagesaeProduktit, " euro")
    
  while pyetja != 'ndalu':
    blej_produktin = input("Deshironi ta bleni produktin?. Shtypni 'po' ose 'jo'! ")
    if blej_produktin == 'po':
      pagesa_totale = pagesa_totale + pagesaeProduktit
      print("Totali i pageses suaj eshte: %.2f" %pagesa_totale, "euro.")
      pyetja = input("Deshironi te vazhdoni me blerjen? Shtypni 'po' ose 'jo'! ")
      if pyetja == 'po':
        produkt = eval(input("Ju lutem shkruani produktin qe deshironi te blini! "))
        if produkt.njesia_matese == 'kg':
          sasia = float(input("Ju lutem shkruani sasine ne kilogram! (P.sh 0.30"))
        else:
          sasia = int(input("Ju lutem shkruani sasine ne cope! "))
      if pyetja == 'jo':
        print("Totali i pageses suaj eshte: %.2f" %pagesa_totale, "euro.")
        break
    elif blej_produktin == 'jo':
       pyetja = input("Deshironi ta ndalni blerjen? Shtypni 'ndalu' ose 'vazhdo'! ")
       if pyetja == 'vazhdo':
         produkt = eval(input("Ju lutem shkruani produktin qe deshironi te blini! "))
         if produkt.njesia_matese == 'kg':
            sasia = float(input("Ju lutem shkruani sasine ne kilogram! (P.sh 0.30"))
         else:
            sasia = int(input("Ju lutem shkruani sasine ne cope! "))
       else:
         print("Totali i pageses suaj eshte: %.2f" %pagesa_totale, "euro.")
         break
    else:
      print("Fjala nuk eshte e vlefshme!")
      produkt = eval(input("Ju lutem shkruani produktin qe deshironi te blini! "))
      if produkt.njesia_matese == 'kg':
        sasia = float(input("Ju lutem shkruani sasine ne kilogram! (P.sh 0.30"))
      else:
        sasia = int(input("Ju lutem shkruani sasine ne cope! "))
  #print(pagesa_totale) 
main()










