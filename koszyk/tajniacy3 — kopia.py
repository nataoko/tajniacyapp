#okno z kartami 25 z haslami z slowa25 - zrobione
#po najechaniu na karte, zmienia sie kolor - zrobione
#po kliknieciu zmienia na kolor druzyny [badx obrazek ladny] - zrobione
#kursor to reka - zrobione
#zrobić karte i ja zapisac - zrobione
#zmienic tlo karty na jdnolity - zrobione
#uruchomic ponownie po wygranej jednej z druzyn - zrobione
#zmienic clicka -zrobione
#menu: instrukcja, o autorze, nowa gra - zrobione
#po zakończeniu rundy dodć powrót do menu - zrobione
# dodac zmienne globalne, zebynie otwierac plikow milion razy - ok
# czcionka


import pygame
from pygame.locals import *
import os.path
import random
import sys


#sorted(pygame.font.get_fonts())
czcionka = 'calibri'#'twcenpogrubiony'#'aharoni'
czcionka2 = 'calibri' #monospace
fontsize = 35
fontsize2 = 18
fontsize30 = 25
fontpogrubiony = 1
fontpogrubionyboard = 1


# funkcje pomocnicze........................................................

def liczby25(l_wyrazow):
    """Zwraca 25 różnych liczb calkowitych z zakresu liczb [0, l_wyrazow-1]."""

    Liczby = []
    
    while len(Liczby)<25:
        
        liczba = int(random.random()*l_wyrazow) #generuje nowa liczbe calkowita
        powt = 0 #zmienna sprawdzajaca, czy liczba juz jest w Liczby
        
        for i in range(len(Liczby)):
          if Liczby[i] == liczba:
            powt = 1
            break
        
        if powt == 0:
          Liczby.append(liczba)
          
    return(Liczby)



def slowa25():
    """zwraca 25 slow. Funkcja pobiera slowa z pliku slowa250.txt
        i przepisuje do pliku slowa250v2.txt.
        Jezeli wszystki slowa beda przepisane - pliki zamieniaja sie nazwami
        i funkcja dziala."""
    
    to_copy=''
    to_copy_zmiana =''
    Slowa25=[]
    k=[]

            
    with open('data'+os.sep+'slowa250.txt','r', encoding="utf8") as file1:
    #Przepisuje tekst z pierwotnego pliku linia po linii.
        for line in file1:
          to_copy+=line
          k.append(line)
          
    if len(k) == 25:
        Slowa25 = [k[i][:-1] for i in range(25)]
        with open('data'+os.sep+'slowa250v2.txt','r', encoding="utf8") as file_zmiana:
        #Przepisuje tekst z pierwotnego pliku linia po linii.
          for line in file_zmiana:
            to_copy_zmiana+=line

        copy1_zmiana=open('data'+os.sep+'slowa250.txt','w',encoding="utf8")
        #Tworzy pustą kopię pliku, do której wpisuje treść oryginalnego pliku tekstowego.
        copy1_zmiana.write(to_copy_zmiana)
        copy1_zmiana.close()

        copy_zmiana = open('data'+os.sep+'slowa250v2.txt','w',encoding="utf8")
        copy_zmiana.write(to_copy)
        copy_zmiana.close()
        #print('zmiana nazwy') 
    else:
        Liczby = liczby25(len(k))
        Liczby.sort()
  
        copy=open('data'+os.sep+'slowa250.txt','w',encoding="utf8")
        #Tworzy pustą kopię pliku, do której wpisuje treść oryginalnego pliku tekstowego.

        copy1 = open('data'+os.sep+'slowa250v2.txt','a',encoding="utf8")
        #open for writing, appending to the end of the file if it exists

        
        for i in range(len(k)):
            try:
                if i == Liczby[0]:
                    Slowa25.append(k[i][:-1])
                    Liczby = Liczby[1:]
                    copy1.write(k[i])
                else:
                    copy.write(k[i])
            except IndexError:
                copy.write(k[i])
                
        copy.close()
        copy1.close()
    
        
    return Slowa25



def krata():
    """Zwraca ciąg 26ciu cyfr. 
        Pierwsza cyfra to 2 lub 3 i oznacza,
        że zaczynają(9 pola zaczynaja) odpowiednio czerwoni lub niebiescy.
        Dalsze cyfry to w kolejnosci losowej: jedno 0 oznaczający czarne pole,
        siedem 1-białe, osiem lub dziewięć 2 i 3- czerwone i niebieskie."""
    lista0 =[0,2,3]
    lista0.extend([1 for i in range(7)])
    lista0.extend([2 for i in range(7)])
    lista0.extend([3 for i in range(7)])#lista0 z tyle ile w opisie
    lista = []
    
    if random.random()<0.5:
        lista.append(2)
        lista0.append(2)
    else:
        lista.append(3)
        lista0.append(3)
        
    while len(lista0)>0:
        i = int(random.random()*(len(lista0)))
        lista.append(lista0[i])
        lista0 = lista0[:i]+lista0[(i+1):]

    return lista

#...................................................................

      
def rysunek(Kolory):
    """Tworzy w current katalogu rysunke z plansza dla szefow gry o nazwie dla_szefow.
        Podac liste kolorow."""
    background_image1 = pygame.image.load(os.path.join("data","bkg1.jpg"))  #plik -> płaszczyzna
    szer1 = background_image1.get_width()
    Lista =[];
    [Lista.append([int(szer1/7+(szer1/7-50)/2)+(i%5)*int(szer1/7), int(szer1/7+(szer1/7-50)/2)+(int(i/5))*int(szer1/7), Kolory[i]]) for i in range (25)]

    for i in range(25):
            kwadr_szer = Lista[i][0]
            kwadr_wys = Lista[i][1]
            kwadr_kolor = Lista[i][2]
            if kwadr_kolor == 0:
                image=pygame.image.load(os.path.join("data","KartaCzarna_mala.png"))
            if kwadr_kolor == 1:
                image=pygame.image.load(os.path.join("data","KartaBiala_mala.png"))
            if kwadr_kolor == 2:
                image=pygame.image.load(os.path.join("data","KartaCzerwona_mala.png"))
            if kwadr_kolor == 3:
                image=pygame.image.load(os.path.join("data","KartaNiebieska_mala.png"))
            background_image1.blit(image,(kwadr_szer,kwadr_wys))
    saveImage(background_image1,"dla_szefow.jpg")


def saveImage(name,nazwa_pliku):
    """Zapisuje obraz name pod nazwa nazwa_pliku w current kataogu"""

    pygame.image.save(name,nazwa_pliku)

def loadImage(name, useColorKey=False):
    """ Załaduj obraz i przekształć go w powierzchnię.

    Funkcja ładuje obraz z pliku i konwertuje jego piksele 
    na format pikseli ekranu. Jeśli flaga useColorKey jest 
    ustawiona na True, kolor znajdujący się w pikselu (0,0)
    obrazu będzie traktowany jako przezroczysty (przydatne w 
    przypadku ładowania obrazów statków kosmicznych)
    """
    fullname = os.path.join("data",name)
    image = pygame.image.load(fullname)  #plik -> płaszczyzna
    image = image.convert() #przekonwertuj na format pikseli ekranu
    if useColorKey is True:
        colorkey = image.get_at((2,2)) #odczytaj kolor w punkcie (0,0)
        image.set_colorkey(colorkey,RLEACCEL) # ustaw kolor jako przezroczysty
        #flaga RLEACCEL oznacza lepszą wydajność na ekranach bez akceleracji
        #wymaga from pygame.locals import *
    return image

#def ramka(file):
    #start=loadImage("RAMKA.png")
    
#    return odczyt(file)

def odczyt(file):
    '''wczytuje tekst z pliku i zwraca linie w liscie'''
    myfont = pygame.font.SysFont(czcionka2, fontsize2 ,bold = 1)
    i=0
    Labels = []
    with open('data'+os.sep+file,'r') as file1:
        #Przepisuje tekst pliku linia po linii.
        for line in file1:
          i+=10
          # render text
          label = myfont.render(line[0:-1], 1, (0,0,0))
          #screen.blit(label, (SCREEN_WIDTH/3+10+255,200+3+i))
          #screen.blit(label, (int(SCREEN_WIDTH/5),160+i))
          Labels.append(label)
    return Labels

def ramka(Labels):
    "wywala na ekranie Labels (tabela z liniami)"
    screen.blit(background_image_jasny,(0,0))
    i = 0
    for label in Labels:
        i += 10
        screen.blit(label, (int(SCREEN_WIDTH/5),160+i))

def game_loop():   
    
    running = True
    INTRO = 2
    kartaSprites = pygame.sprite.RenderClear() #init kart do menu
    kartaSprites.add(menu_nowa_gra)
    kartaSprites.add(menu_instrukcja)
    kartaSprites.add(menu_o_autorze)

    kursorSprite = pygame.sprite.RenderClear() # init kursora
    kursorSprite.add(kursor)
    #background_image=loadImage("bkg.jpg")
    
    while running:
        clock.tick(40) #nie więcej niż 40 klatek na sekundę
        #screen.blit(background_image,(0,0))
        kursorSprite.clear(screen, kursor.background_image)

            
        if INTRO == 2: # menu
            if menu_o_autorze.open:
                ramka(autortxt)
                menu_instrukcja.open = 0
            if menu_instrukcja.open:
                ramka(instrutxt)
                menu_o_autorze.open = 0

            #uaktualnij sprite'y
            kartaSprites.update() 

            #rysuj sprite'y
            kartaSprites.draw(screen) 
         
        if INTRO == 1: #po zakonczenu gry

            #dodaje i uaktualnia sprity
            kartaSprites.add(nowa_gra)
            kartaSprites.add(menu)
            nowa_gra.update() #uaktualnia tylko nowa_gra
            menu.update()
            kartaSprites.draw(screen) #dodaje karte nowa_gra, menu

            
        if INTRO == 0: #gra
            kartaSprites.update()#update kart
            
            #Wyczyść ekran
            scoreboardredSprite.clear(screen, background_image)
            scoreboardblueSprite.clear(screen,background_image)
            kartaSprites.clear(screen,background_image)            
            
            #rysuj sprite'y na ekranie
            scoreboardredSprite.draw(screen)
            scoreboardblueSprite.draw(screen)
            kartaSprites.draw(screen)

            #Sprawdź, czy ktos wygral
            if scoreboardred.score == (8+ (kol_dom==2)) or \
               scoreboardblue.score == (8+ (kol_dom==3)) or \
               karta_czarna.czy_czarna_odkryta==1:
                INTRO=1

        if menu.counter == 2: # jezeli menu klikniete

            #wyczysc sprite'y kart
            kartaSprites.clear(screen,background_image_t)
            kartaSprites = pygame.sprite.RenderClear() #kontener

            #dodaj karty
            kartaSprites.add(menu_nowa_gra)
            kartaSprites.add(menu_instrukcja)
            kartaSprites.add(menu_o_autorze)

            INTRO = 2
            
            kursor.background_image = background_image_t
            screen.blit(background_image_t,(0,0)) 
            
            menu.counter = 0
         
        if nowa_gra.counter == 2 or menu_nowa_gra.counter == 2:
            menu_instrukcja.open = 0
            menu_o_autorze.open = 0
            kursor.background_image = background_image
            screen.blit(background_image,(0,0))

            #wyczysc sprite'y kart
            kartaSprites.clear(screen,background_image)
            kartaSprites = pygame.sprite.RenderClear() #kontener
            
            Kolory = krata()
            kol_dom = Kolory[0] #kolor dominujacy
            Kolory = Kolory[1:]#kolory

            rysunek(Kolory)#tworzenie rysunka 

            #Inicjalizuj karty
            Slowa = slowa25() #slowa
               
            for i in range (25):
                kolor = Kolory[i]
                slowo = Slowa[i]
                if kolor ==0:
                    karta_czarna = Karta(startx+(i%5)*karta.szer, starty+(int(i/5))*karta.wys, slowo, kolor)
                    kartaSprites.add(karta_czarna)
                else:
                    kartaSprites.add(Karta(startx+(i%5)*karta.szer, starty+(int(i/5))*karta.wys, slowo, kolor))


            scoreboardred.pkty = 8 + (kol_dom == 2) #/pkty
            scoreboardblue.pkty = 8 + (kol_dom == 3) #/pkty
            scoreboardredSprite.update(-scoreboardred.score) #0/ +uaktualnia wynik, czyli 0/pkty
            scoreboardblueSprite.update(-scoreboardblue.score) #0/ +uaktualnia wynik, czyli 0/pkty
            
            INTRO = 0
            
            nowa_gra.counter = 0
            menu_nowa_gra.counter = 0
        
        kursor.update()
        kursorSprite.draw(screen)
        pygame.display.flip() #aktualizacja całej sceny
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                
    pygame.quit()
    sys.exit()
#....................................................................................................

class Kursor(pygame.sprite.Sprite):
    """Kursor"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.mouse.set_visible(0)
        self.image = loadImage('mysz.png',True)
        self.rect = pygame.mouse.get_pos()
        self.background_image = background_image_t
    def update(self):
        self.pos = pygame.mouse.get_pos()
        #screen.blit(self.image,self.pos)
        self.rect = pygame.mouse.get_pos()

class Karta(pygame.sprite.Sprite):
    """Klasa kart"""
    def __init__(self,startx, starty, slowo, kolor):
        #inicjalizuj klasę bazową
        pygame.sprite.Sprite.__init__(self)
        self.kolor = kolor
        self.image = loadImage("Karta.png",True)
        self.szer = self.image.get_width()
        self.wys = self.image.get_height()
        self.text = slowo
        self.rect = self.image.get_rect()
        self.startx = startx
        self.starty = starty
        self.rect.centerx = startx
        self.rect.centery = starty       
        self.font = pygame.font.SysFont(czcionka,fontsize30, fontpogrubiony)
        self.imageT = self.font.render(self.text,1,(0,0,0))
        self.image.blit(self.imageT,(int(self.szer/10),int(self.wys/3)))
        self.counter = 0
        self.czy_czarna_odkryta = 0
        self.open = 0
        
    def update(self):
     
      if self.counter < 2:
           if (self.startx-self.szer/2)<=pygame.mouse.get_pos()[0]<=(self.startx+self.szer/2)\
              and (self.starty-self.wys/2)<=pygame.mouse.get_pos()[1]<=(self.starty+self.wys/2):
                self.image = loadImage("Karta1.png",True)#zmiana koloru
                self.image.blit(self.imageT,(int(self.szer/10),int(self.wys/3))) #tekst
                
                if pygame.mouse.get_pressed()[0]: #klik
                    self.counter = 1 
                if pygame.mouse.get_pressed()[0] !=1 and self.counter ==1: #klik i puszczenie                
                        self.counter = 2 #karta nieaktywna
                        if self.kolor == 0:
                            self.image = kartaczarna
                            self.czy_czarna_odkryta = 1
                        elif self.kolor == 1:
                            self.image = kartabiala
                        elif self.kolor == 2:
                            self.image = kartaczerwona
                            scoreboardredSprite.update()
                        elif self.kolor == 3:
                            self.image = kartaniebieska
                            scoreboardblueSprite.update()
                        elif self.kolor == 4: # instrukcja
                            ramka(instrutxt)
                            self.image = loadImage("Karta.png",True)
                            self.image.blit(self.imageT,(int(self.szer/10),int(self.wys/3)))
                            kursor.background_image = background_image
                            menu_o_autorze.open = 0
                            self.counter = 0
                            self.open = 1
                        elif self.kolor == 5: # o autorze
                            ramka(autortxt)
                            self.image = loadImage("Karta.png",True)
                            self.image.blit(self.imageT,(int(self.szer/10),int(self.wys/3)))
                            kursor.background_image = background_image
                            menu_instrukcja.open = 0
                            self.counter = 0
                            self.open = 1

           else:
            self.counter = 0
            self.image = loadImage("Karta.png",True)
            self.image.blit(self.imageT,(int(self.szer/10),int(self.wys/3)))
            

class ScoreBoardRed(pygame.sprite.Sprite):
    def __init__(self):
        #inicjalizuj klasę bazową
        pygame.sprite.Sprite.__init__(self)
        self.czy_dominuje = 1
        self.score = 0
        self.pkty = 8+self.czy_dominuje
        self.text = "CZERWONI: 0 / %1d"  % self.pkty
        self.font = pygame.font.SysFont(czcionka,fontsize, fontpogrubionyboard)
        self.image = self.font.render(self.text,1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.left=int(SCREEN_WIDTH*(1/8))
        self.rect.top=int(SCREEN_HEIGHT*(1/16))

    def update(self,a=1):
        self.score += a
        myorder = "CZERWONI: {} / {}"
        self.text = myorder.format(self.score, self.pkty)
        self.image = self.font.render(self.text,1,(0,0,0))
        
class ScoreBoardBlue(pygame.sprite.Sprite):
    def __init__(self):
        #inicjalizuj klasę bazową
        pygame.sprite.Sprite.__init__(self)
        self.czy_dominuje = 1
        self.score = 0
        self.pkty = 8+self.czy_dominuje
        self.text = "NIEBIESCY: 0 / %1d"  % self.pkty
        self.font = pygame.font.SysFont(czcionka,fontsize, fontpogrubionyboard)
        self.image = self.font.render(self.text,1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.left=int(SCREEN_WIDTH*(5/8))
        self.rect.top=int(SCREEN_HEIGHT*(1/16))
        
    def update(self,a=1):
        self.score += a
        myorder = "NIEBIESCY: {} / {}"
        self.text = myorder.format(self.score, self.pkty)
        #self.text = "NIEBIESCY: %1d" % self.score
        self.image = self.font.render(self.text,1,(0,0,0))

if __name__ == '__main__':
    # właściwy program
    # Inicjalizacja PyGame
    pygame.init()

    SCREEN_WIDTH = 1019 
    SCREEN_HEIGHT = 740 #wymiary ekranu
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #tworzy okno 
    pygame.display.set_caption("TAJNIACY") #dodaje tytuł
    background_image = loadImage("bkg.jpg")#ładuje plik z tłem
    background_image_t = loadImage("bkg_t.jpg")
    background_image_jasny = loadImage("bkg_tlo_jasne.png")
    screen.blit(background_image_t,(0,0)) #dodaje tło

    kartaczarna = loadImage("KartaCzarna.png",True)
    kartabiala = loadImage("KartaBiala.png",True)
    kartaczerwona = loadImage("KartaCzerwona.png",True)
    kartaniebieska = loadImage("KartaNiebieska.png",True) 

    autortxt =  odczyt('autor.txt')
    instrutxt = odczyt('instru.txt')
    
    clock = pygame.time.Clock()

    
    # kursor
    kursor = Kursor()
    
    # Inicjalizacja zmienne kontrolne
    startx = 110
    starty = 150
    karta = Karta(startx, starty, 'proba', 1)
    nowa_gra = Karta(int(SCREEN_WIDTH/2), int(karta.wys/2), 'NOWA GRA', 1)
    menu_nowa_gra = Karta(int(SCREEN_WIDTH/2), int(karta.wys/2), 'NOWA GRA', 1)
    menu_instrukcja = Karta(int(SCREEN_WIDTH/4), int(karta.wys/2), 'INSTRUKCJA', 4)
    menu_o_autorze = Karta(int(SCREEN_WIDTH/4+SCREEN_WIDTH/2), int(karta.wys/2), 'O AUTORZE', 5)
    menu = Karta(int(SCREEN_WIDTH/2), SCREEN_HEIGHT -int(karta.wys/2), 'MENU', 1)
    
    # Inicjalizuj punkty czerwonych
    scoreboardredSprite = pygame.sprite.RenderClear()#kontener
    scoreboardred = ScoreBoardRed()
    scoreboardredSprite.add(scoreboardred)

    # Inicjalizuj punkty niebieskich
    scoreboardblueSprite = pygame.sprite.RenderClear()#kontener
    scoreboardblue=ScoreBoardBlue()
    scoreboardblueSprite.add(scoreboardblue) 

    game_loop()
