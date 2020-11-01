#okno z kartami 25 z haslami z slowa25 - zrobione
#po najechaniu na karte, zmienia sie kolor - zrobione
#po kliknieciu zmienia na kolor druzyny [badx obrazek ladny] - zrobione
#kursor to reka
#zrobić karte i ja zapisac
#zmienic tlo karty na jdnolity
#uruchomic ponownie po wygranej jednej z druzyn
#zmienic clicka


import pygame
from pygame.locals import *
import os.path
import random
import os.path


SCREEN_WIDTH = 1019
SCREEN_HEIGHT = 740



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
        print('zmiana nazwy') 
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

    

def game_intro():
    """Początkowy ekran"""

    #odleglosc = 42
    #pocz_wysokosc
    start=loadImage("START.png",True)
    screen.blit(start,(SCREEN_WIDTH/3,200))
    instr=loadImage("INSTR.png",True)
    screen.blit(instr,(SCREEN_WIDTH/3,242))
    autor=loadImage("AUTOR.png",True)
    screen.blit(autor,(SCREEN_WIDTH/3,284))
    koniec=loadImage("KONIEC.png",True)
    screen.blit(koniec,(SCREEN_WIDTH/3,326))
    pygame.mouse.set_visible(1)#kursor
    
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Koniec()
        for i in [(200,242,0),(242,284,'inst'),(284,326,'Wyniki'),(326,368,'Autor'),(368,410,'Koniec')]:
            if button(i)==0:
                intro=0
                return
            
##            else:
##                while SCREEN_WIDTH/3+203<=pygame.mouse.get_pos()[0]<=SCREEN_WIDTH/3+230 and 213<=pygame.mouse.get_pos()[1]<233:
##                      if pygame.mouse.get_pressed()[0]:
##                            print('a')        

        pygame.display.update()
        clock.tick(15)
    return intro

        
def odczyt(file):
    '''wczytuje tekst z pliku'''
    myfont = pygame.font.SysFont("monospace", 15)
    i=0
    with open('data'+os.sep+file,'r') as file1:
        #Przepisuje tekst pliku linia po linii.
        for line in file1:
          i+=10
          # render text
          label = myfont.render(line[0:-1], 1, (255,0,255))
          screen.blit(label, (SCREEN_WIDTH/3+10+255,200+3+i))
    return 1


def Ramka(file):
    start=loadImage("RAMKA.png")
    screen.blit(start,(SCREEN_WIDTH/3+250,200))
    #pygame.draw.rect(screen, (255,255,255),(SCREEN_WIDTH/3+10,200+3,230,200))
##    pygame.draw.rect(screen, (255,0,255),(SCREEN_WIDTH/3+200,200+3+10,20,20))
##    myfont = pygame.font.SysFont("arial", 30)
##    label = myfont.render('X', 1, (255,255,255))
##    screen.blit(label, (SCREEN_WIDTH/3+202,206))
    odczyt(file)



def button1(left, right, up, down):
    wynik=1 #get the state of the mouse buttons #get the mouse cursor position
    if left<=pygame.mouse.get_pos()[0]<=right and down<=pygame.mouse.get_pos()<=up:
        start=loadImage("RAMKA.png",True)
        screen.blit(start,(left,up))
        if pygame.mouse.get_pressed()[0]:
            if i[2]==0:
                wynik=0
            elif i[2]=='inst':
                Ramka('instru.txt')
            elif i[2]=='Autor':
                Ramka('autor.txt')
            else:
                pygame.quit()
                quit()
    return wynik


def button(i):
    wynik=1 #get the state of the mouse buttons #get the mouse cursor position
    if SCREEN_WIDTH/3<=pygame.mouse.get_pos()[0]<=SCREEN_WIDTH/3+253 and i[0]<=pygame.mouse.get_pos()[1]<i[1]:
        if pygame.mouse.get_pressed()[0]:
            if i[2]==0:
                wynik=0
            elif i[2]=='inst':
                Ramka('instru.txt')
            elif i[2]=='Autor':
                Ramka('autor.txt')
            else:
                pygame.quit()
                quit()
    return wynik

##def Start():
##    print('star')
##    return False
      

def Koniec():
    pygame.quit()
    quit()


def saveImage(name):
    """Zapisuje obraz"""

    pygame.image.save(name,"rys.jpg")

    
    return 'zapisano'
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

#....................................................................................................




class Karta(pygame.sprite.Sprite):
  
    def __init__(self,startx, starty, slowo, kolor):
        #inicjalizuj klasę bazową
        pygame.sprite.Sprite.__init__(self)
        self.kolor = kolor
        self.image = loadImage("Karta.png", True)
        self.szer = self.image.get_width()
        self.wys = self.image.get_height()
        self.text = slowo
        self.rect = self.image.get_rect()
        self.startx = startx
        self.starty = starty
        self.rect.centerx = startx
        self.rect.centery = starty       
        self.font = pygame.font.SysFont(None,30)
        self.imageT = self.font.render(self.text,1,(0,0,0))
        self.image.blit(self.imageT,(int(self.szer/10),int(self.wys/3)))
        self.counter = 0
        
    def update(self):
      
      if self.counter == 0:
       if (self.startx-self.szer/2)<=pygame.mouse.get_pos()[0]<=(self.startx+self.szer/2) and (self.starty-self.wys/2)<=pygame.mouse.get_pos()[1]<=(self.starty+self.wys/2):
        self.image=loadImage("Karta1.png",True)
        self.image.blit(self.imageT,(int(self.szer/10),int(self.wys/3)))
        #screen.blit(start,(left,up))
        if pygame.mouse.get_pressed()[0]:
            if self.kolor == 0:
                self.image=loadImage("KartaCzarna.png",True)
            if self.kolor == 1:
                self.image=loadImage("KartaBiala.png",True)
            if self.kolor == 2:
                self.image=loadImage("KartaCzerwona.png",True)
                scoreboardredSprite.update()
            if self.kolor == 3:
                self.image=loadImage("KartaNiebieska.png",True)
                scoreboardblueSprite.update()
            self.counter = 1
                
       else:
        self.image=loadImage("Karta.png",True)
        self.image.blit(self.imageT,(int(self.szer/10),int(self.wys/3)))        
           

class ScoreBoardRed(pygame.sprite.Sprite):
    def __init__(self, czy_dominuje):
        #inicjalizuj klasę bazową
        pygame.sprite.Sprite.__init__(self)
        self.score = 0
        self.pkty = 8+czy_dominuje
        self.text = "CZERWONI: 0 / %1d"  % self.pkty
        self.font = pygame.font.SysFont(None,40)
        self.image = self.font.render(self.text,1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.left=int(SCREEN_WIDTH*(1/8))
        self.rect.top=int(SCREEN_HEIGHT*(1/16))

    def update(self,a=1):
        self.score += a
        myorder = "CZERWONI: {} / {}"
        self.text = myorder.format(self.score, self.pkty)
        self.image = self.font.render(self.text,1,(0,0,0))
        #self.rect = self.image.get_rect()
        #self.rect.left=int(SCREEN_WIDTH*(1/8))
        #self.rect.top=int(SCREEN_HEIGHT*(1/16))
        
class ScoreBoardBlue(pygame.sprite.Sprite):
    def __init__(self, czy_dominuje):
        #inicjalizuj klasę bazową
        pygame.sprite.Sprite.__init__(self)
        self.score = 0
        self.pkty = 8+czy_dominuje
        self.text = "NIEBIESCY: 0 / %1d"  % self.pkty
        #self.text = "NIEBIESCY: %1d " % self.score
        self.font = pygame.font.SysFont(None,40)
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
        #self.rect = self.image.get_rect()
        #self.rect.left=int(SCREEN_WIDTH*(5/8))
        #self.rect.top=int(SCREEN_HEIGHT*(1/16))


if __name__ == '__main__':
    # właściwy program

    # Inicjalizacja PyGame
    pygame.init()

    #tworzenie rysunka
    Kolory = krata()
    kol_dom = Kolory[0]
    Kolory = Kolory[1:]#kolory
    szer1 = 450
    Lista =[];
    [Lista.append([int(szer1/7+(szer1/7-50)/2)+(i%5)*int(szer1/7), int(szer1/7+(szer1/7-50)/2)+(int(i/5))*int(szer1/7), Kolory[i]]) for i in range (25)]
    screen2 = pygame.display.set_mode((szer1,szer1))
    background_image1=loadImage("bkg1.jpg")#ładuje plik z tłem
    screen2.blit(background_image1,(0,0))
    #if kol_dom == 2:
    #    bok = loadImage("KartaCzerwona_bok.png")
    #    gora = loadImage("KartaCzerwona_gora.png")
    #    screen2.blit(gora,(int(szer1/2),int(szer1/14)))
    for i in range(25):
            if Lista[i][2] == 0:
                image=loadImage("KartaCzarna_mala.png")
            if Lista[i][2] == 1:
                image=loadImage("KartaBiala_mala.png")
            if Lista[i][2] == 2:
                image=loadImage("KartaCzerwona_mala.png")
            if Lista[i][2] == 3:
                image=loadImage("KartaNiebieska_mala.png")
            screen2.blit(image,(Lista[i][0],Lista[i][1]))
    print(saveImage(screen2))

    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #tworzy okno 
    pygame.display.set_caption("TAJNIACY") #dodaje tytuł
    background_image=loadImage("bkg.jpg")#ładuje plik z tłem
    screen.blit(background_image,(0,0)) #dodaje tło


    ### Załaduj pliki audio
    ###frogFX = loadSound("explode.wav")
    ###bocianFX=loadSound("explode.wav")


    #Inicjalizuj karty
    Slowa = slowa25() #slowa
    startx = 110
    starty = 150
    karta = Karta(startx, starty, 'proba', 1)
    kartaSprites = pygame.sprite.RenderClear() #kontener
    
    for i in range (25):
        kolor = Kolory[i]
        slowo = Slowa[i]
        kartaSprites.add(Karta(startx+(i%5)*karta.szer, starty+(int(i/5))*karta.wys, slowo, kolor))
    
    # Inicjalizuj punkty czerwonych
    scoreboardredSprite = pygame.sprite.RenderClear()#kontener
    scoreboardred=ScoreBoardRed((kol_dom == 2))
    scoreboardredSprite.add(scoreboardred)

    # Inicjalizuj punkty niebieskich
    scoreboardblueSprite = pygame.sprite.RenderClear()#kontener
    scoreboardblue=ScoreBoardBlue((kol_dom == 3))
    scoreboardblueSprite.add(scoreboardblue)


    # Inicjalizuj zmienne kontrolne
    clock = pygame.time.Clock()
    running = True
    ##bocianCounter = 0
    ##muchaCounter = 0
    #score=0
    #lifes=3
    INTRO=1

    while running:
        clock.tick(40) #nie więcej niż 40 klatek na sekundę
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                Koniec()
        if INTRO:
        #    INTRO= game_intro()
        #else:
            screen.blit(background_image,(0,0))
        #    pygame.mouse.set_visible(0)#kursor niewidoczny
        

    ##    #Sprawdź, czy ktos wygral
    ##       scoreboardred.score() == 8+ (czy_dominuje==2)             
    ##            INTRO=1
    ##            
    ##
            kartaSprites.update()
            #Wyczyść ekran
            scoreboardredSprite.clear(screen, background_image)
            scoreboardblueSprite.clear(screen,background_image)
            kartaSprites.clear(screen,background_image)
            print(scoreboardred.score)
            
            #rysuj sprite'y na ekranie
            scoreboardredSprite.draw(screen)
            scoreboardblueSprite.draw(screen)
            kartaSprites.draw(screen)
                    
            pygame.display.flip() #aktualizacja całej sceny