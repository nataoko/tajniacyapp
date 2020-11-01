import random
import os.path
    
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
    lista0.extend([3 for i in range(7)])
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



if __name__ == '__main__':            
 print(slowa25())
