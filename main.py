from background import *
import random,turtle,time

background()

pyetja_produktit = turtle.textinput("Produkti","Cfare produkti deshironi te blini?")
#global produkt
produkt = eval(pyetja_produktit)

if produkt.njesia_matese == 'kg':
    pyetja_sasise1 = turtle.textinput("Sasia","Shkruani sasine ne kg! P.sh 0.30")
    produkt.sasia = float(pyetja_sasise1)
else:
    pyetja_sasise2 = turtle.textinput("Sasia","Shkruani sasine ne cope!")
    produkt.sasia = int(pyetja_sasise2)
    
def main():
  pagesa_totale = 0
  # Variabla per te ju pergjigjur programit
  pyetja = ('po', 'jo', 'ndalu')
  lajmerim = ''
  global produkt
  
  if produkt in pijetMeOferte:
      pagesa = produkt.pagesaPerPije()
      pagesaeProduktit = "Cmimi eshte: %.2f" %pagesa, "€. Shkruani 'po' ose 'jo' per blerje"
      
  elif produkt in pijetPaOferte:
      pagesa = produkt.pagesaPijePaOferte()
      pagesaeProduktit = "Cmimi eshte: %.2f" %pagesa, "€. Shkruani 'po' ose 'jo' per blerje"
      
  elif produkt in frutat:
      pagesa = produkt.pagesaPerFruta()
      pagesaeProduktit = "Cmimi eshte: %.2f" %pagesa, "€. Shkruani 'po' ose 'jo' per blerje"
      

  while pyetja != 'ndalu':
      blej_produktin = turtle.textinput("Deshironi ta bleni? ", pagesaeProduktit)
      
      if blej_produktin == 'po':
          pagesa_totale = pagesa_totale + pagesa
          totaliipageses = "Totali i pageses suaj eshte: %.2f" %pagesa_totale, "euro. Shtypni OK"
          pyetja = turtle.textinput("Deshironi te vazhdoni me blerjen?", "Deshironi te vazhdoni me blerjen?. Shkruani 'po' ose 'jo'!")
          
          if pyetja == 'po':
                pyetja_produktit = turtle.textinput("Produkti","Cfare produkti deshironi te blini?")
                produkt = eval(pyetja_produktit)
                if produkt.njesia_matese == 'kg':
                    pyetja_sasise1 = turtle.textinput("Sasia","Shkruani sasine ne kg! P.sh 0.30")
                    produkt.sasia = float(pyetja_sasise1)
                else:
                    pyetja_sasise2 = turtle.textinput("Sasia","Shkruani sasine ne cope!")
                    produkt.sasia = int(pyetja_sasise2)
                if produkt in pijetMeOferte:
                    pagesa = produkt.pagesaPerPije()
                    pagesaeProduktit = "Cmimi eshte: %.2f" %pagesa, "€. Shkruani 'po' ose 'jo' per blerje"
                    
                elif produkt in pijetPaOferte:
                    pagesa = produkt.pagesaPijePaOferte()
                    pagesaeProduktit = "Cmimi eshte: %.2f" %pagesa, "€. Shkruani 'po' ose 'jo' per blerje"
                    
                elif produkt in frutat:
                    pagesa = produkt.pagesaPerFruta()
                    pagesaeProduktit = "Cmimi eshte: %.2f" %pagesa, "€. Shkruani 'po' ose 'jo' per blerje"
                
                
          if pyetja == 'jo':
              totaliipageses = "Totali i pageses suaj eshte: %.2f" %pagesa_totale, "euro."
              cmimieshte = turtle.textinput("Pagesa", totaliipageses)
              
              break
      elif blej_produktin == 'jo':
          pyetja = turtle.textinput("Deshironi ta ndalni blerjen?","Deshironi te vazhdoni me blerjen? Shkruani 'vazhdo' ose 'ndalu'!")
          
          if pyetja == 'vazhdo':
              pyetja_produktit = turtle.textinput("Produkti","Cfare produkti deshironi te blini?")
              
              produkt = eval(pyetja_produktit)
              if produkt.njesia_matese == 'kg':
                  pyetja_sasise1 = turtle.textinput("Sasia","Shkruani sasine ne kg! P.sh 0.30")
                  produkt.sasia = float(pyetja_sasise1)
              else:
                  pyetja_sasise2 = turtle.textinput("Sasia","Shkruani sasine ne cope!")
                  produkt.sasia = int(pyetja_sasise2)
              if produkt in pijetMeOferte:
                  pagesa = produkt.pagesaPerPije()
                  pagesaeProduktit = "Cmimi eshte: %.2f" %pagesa, "€. Shkruani 'po' ose 'jo' per blerje"
              elif produkt in pijetPaOferte:
                  pagesa = produkt.pagesaPijePaOferte()
                  pagesaeProduktit = "Cmimi eshte: %.2f" %pagesa, "€. Shkruani 'po' ose 'jo' per blerje"
              elif produkt in frutat:
                  pagesa = produkt.pagesaPerFruta()
                  pagesaeProduktit = "Cmimi eshte: %.2f" %pagesa, "€. Shkruani 'po' ose 'jo' per blerje"
          else:
              totaliipageses = "Totali i pageses suaj eshte: %.2f" %pagesa_totale, "euro."
              cmimieshte = turtle.textinput("Pagesa", totaliipageses)
              
              break
      else:
          lajmerim = turtle.textinput("Fjala jo e vlefshme","Fjala nuk eshte e vlefshme! Shtypni OK!")
          
          pyetja_produktit = turtle.textinput("Produkti","Cfare produkti deshironi te blini?")
              
          produkt = eval(pyetja_produktit)
          if produkt.njesia_matese == 'kg':
              pyetja_sasise1 = turtle.textinput("Sasia","Shkruani sasine ne kg! P.sh 0.30")
              produkt.sasia = float(pyetja_sasise1)
          else:
              pyetja_sasise2 = turtle.textinput("Sasia","Shkruani sasine ne cope!")
              produkt.sasia = int(pyetja_sasise2)
          if produkt in pijetMeOferte:
              pagesa = produkt.pagesaPerPije()
              pagesaeProduktit = "Cmimi eshte: %.2f" %pagesa, "€. Shkruani 'po' ose 'jo' per blerje"
              
          elif produkt in pijetPaOferte:
              pagesa = produkt.pagesaPijePaOferte()
              pagesaeProduktit = "Cmimi eshte: %.2f" %pagesa, "€. Shkruani 'po' ose 'jo' per blerje"
              
          elif produkt in frutat:
              pagesa = produkt.pagesaPerFruta()
              pagesaeProduktit = "Cmimi eshte: %.2f" %pagesa, "€. Shkruani 'po' ose 'jo' per blerje"
main()










