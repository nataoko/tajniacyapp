import pygame
import tajniacy_apka3 as t


def rysunek(Kolory):
    szer1 = 450 #szerokosc rysunka
    Lista =[];
    [Lista.append([int(szer1/7+(szer1/7-50)/2)+(i%5)*int(szer1/7), int(szer1/7+(szer1/7-50)/2)+(int(i/5))*int(szer1/7), Kolory[i]]) for i in range (25)]
    screen2 = pygame.display.set_mode((szer1,szer1))
    background_image1=t.loadImage("bkg1.jpg")#ładuje plik z tłem
    screen2.blit(background_image1,(0,0))
    #if kol_dom == 2:
    #    bok = loadImage("KartaCzerwona_bok.png")
    #    gora = loadImage("KartaCzerwona_gora.png")
    #    screen2.blit(gora,(int(szer1/2),int(szer1/14)))
    for i in range(25):
            if Lista[i][2] == 0:
                image=t.loadImage("KartaCzarna_mala.png")
            if Lista[i][2] == 1:
                image=t.loadImage("KartaBiala_mala.png")
            if Lista[i][2] == 2:
                image=t.loadImage("KartaCzerwona_mala.png")
            if Lista[i][2] == 3:
                image=t.loadImage("KartaNiebieska_mala.png")
            screen2.blit(image,(Lista[i][0],Lista[i][1]))
    t.saveImage(screen2)
