import random
import pygame
import laevazde_gen1 as genlaevad

vastaselaevadtehtud=0
laev = None
laevadearv = -1
kohad = [["n" for j in range(12)] for i in range(12)]
for n in range(12):
    print(kohad[n])
pygame.init()
laeva_a_l = []
laevax = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
laevad = []
tähed = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", ""]
tähed2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ""]
mooda = ["мимо", "пропущенный", "Möödas!", "Piima järele","You missed!", "Siin ei ole kala!"]
x = []
y = []
ekraani_pind = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Laevade pommitamine")
ekraani_pind.fill((255, 255, 255))
for i in range(11):
    ristkylik5 = pygame.Rect(i * 50 + 90, 0, 10, 600)
    pygame.draw.rect(ekraani_pind, (0, 0, 0), ristkylik5)
    x.append([i * 50, i * 50 + 40])

    ristkylik1 = pygame.Rect(0, i * 50 + 90, 1200, 10)
    pygame.draw.rect(ekraani_pind, (0, 0, 0), ristkylik1)
    y.append([i * 50, i * 50 + 40])

    tekst = str(tähed[i])
    meie_font = pygame.font.SysFont("Arial", 36)
    teksti_pilt = meie_font.render(tekst, False, (25, 25, 155))
    ekraani_pind.blit(teksti_pilt, (i * 50 + 120, 10))

    tekst = str(tähed2[i])
    meie_font = pygame.font.SysFont("Arial", 36)
    teksti_pilt = meie_font.render(tekst, False, (25, 25, 155))
    ekraani_pind.blit(teksti_pilt, (30, i * 50 + 100))

for j in range(11):
    tekst = str(tähed[j])
    meie_font = pygame.font.SysFont("Arial", 36)
    teksti_pilt = meie_font.render(tekst, False, (25, 25, 155))
    ekraani_pind.blit(teksti_pilt, (j * 50 + 720, 10))
    ristkylik5 = pygame.Rect(j * 50 + 690, 0, 10, 600)
    pygame.draw.rect(ekraani_pind, (0, 0, 0), ristkylik5)

pygame.display.flip()


def kordinaadidxy():
    global ristkylik5
    # print(pygame.mouse.get_pos())
    kordinaadid = pygame.mouse.get_pos()
    #print(kordinaadid)
    return kordinaadid


def laevaxy():
    # print(laeva_a_l)
    lx = int(laeva_a_l[0][0] / 50) * 50
    lx2 = int(laeva_a_l[0][1] / 50) * 50
    ly = int(laeva_a_l[1][0] / 50) * 50
    ly2 = int(laeva_a_l[1][1] / 50) * 50

    if lx in laevax and ly in laevax and lx2 in laevax and ly2 in laevax and (abs(
            lx - ly) == 100 and lx2 - ly2 == 0 or abs(lx2 - ly2) == 100 and lx - ly == 0):
        return [lx, lx2], [ly, ly2]  # laevakordinaadid
    return ()

def vastaselaevadejoonistamine(vastaselaev):
    for i in range(12):
        for j in range(12):
            #if laev in vastaselaev[i]:
            j_ = vastaselaev[j][i]
            #print(j_)
            if j_ == "l":
                laev2 = pygame.Rect(i*50+650, j*50+50, 50, 50)
                #print("laev2",laev2)
                pygame.draw.rect(ekraani_pind, (0, 0, 0), laev2)



while laevadearv < 7:
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN and event.key == 27:
        break

    
    a = []
    b = []
    if event.type == pygame.MOUSEBUTTONDOWN:  # hiir all
        kor = kordinaadidxy()
        
        if 599>kor[0]>101 and 101<kor[1]<599:
            color = ekraani_pind.get_at(pygame.mouse.get_pos())
            
            laeva_a_l.append(kor)  # algus
            ruut = pygame.Rect(int(kor[0] / 50) * 50, int(kor[1] / 50) * 50, 40, 40)
            pygame.draw.rect(ekraani_pind, (0, 255, 0), ruut)
            pygame.display.flip()
            ruut = pygame.Rect(int(kor[0] / 50) * 50, int(kor[1] / 50) * 50, 40, 40)
            pygame.draw.rect(ekraani_pind, color, ruut)
            
    if len(laeva_a_l) > 1:
        lxy = laevaxy()  # laevakordinaadid
        print(lxy, "lxy")
        if not lxy == ():
            ax = int(lxy[0][0] / 50) - 1
            ay = int(lxy[0][1] / 50) - 1
            lx = int(lxy[1][0] / 50) - 1
            ly = int(lxy[1][1] / 50) - 1
            print(ax, ay, lx, ly)
            print(laevadearv, "laevadearv")
            print(kohad[ly + 1][lx], " kohad r1")

            if lx < ax and ay == ly:  # tagurpidi laeva kordinaatide vahetus
                l = ax
                ax = lx
                lx = l

            if ax == lx and ly < ay:
                ay, ly = ly, ay

            if lx > ax:  # horisontaalne laev
                Saab = 1
                for x in range(ax, lx + 1):  # kas  saab laeva teha

                    if kohad[ay][x] == "l" or kohad[ay - 1][x] == "l" or kohad[ay + 1][x] == "l":
                        Saab = 0
                if (kohad[ay][ax - 1] == "l" or kohad[ay][lx + 1] == "l"):
                    Saab = 0

                if Saab == 1:
                    laev = pygame.Rect(ax * 50 + 50, lxy[0][1], 150, 50)
                    # print("H: ", laevadearv,ax*50, lxy[0][0], lxy[0][1], hs*150,  50)
                    laevadearv += 1
                    for l in range(3):
                        kohad[ay][ax + l] = "l"
                        # print("Xa: ",lxy[0][0] / 50 - 2)
                        # print("ya: ",lxy[0][1] / 50 - 2 + l)

            elif ly > ay:  # vertikaalne laev
                Saab = 1
                for y in range(ay, ly + 1):  # kas laeva saab
                    if kohad[y][ax] == "l" or kohad[y][ax - 1] == "l" or kohad[y][ax + 1] == "l":
                        Saab = 0
                if (kohad[ay - 1][ax] == "l" or kohad[ly + 1][ax] == "l"):
                    Saab = 0

                if Saab == 1:
                    laev = pygame.Rect(lxy[0][0], ay * 50 + 50, 50, 150)
                    laevadearv += 1
                    for l in range(3):
                        kohad[ay + l][ax] = "l"

            for n in range(12):
                print(n, " - ", kohad[n])
            pygame.draw.rect(ekraani_pind, (0, 0, 0), laev)
            pygame.display.flip()
        laeva_a_l.clear()

    if event.type == pygame.QUIT:
        break

vastaselaevadtehtud=1
vastaselaevad = genlaevad.Pane_Laevad_Paigale()  # vastaselaevad
print("Arva ära, kus on minu laevad!")


pygame.display.flip()

    
pohjas=0
while True:
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN and event.key == 27:
        break    
        
    if event.type == pygame.MOUSEBUTTONDOWN:  # hiir all
        kor = kordinaadidxy()
        color = ekraani_pind.get_at(pygame.mouse.get_pos())
        if 701<kor[0]<1199 and 101<kor[1]<599:
            ruut = pygame.Rect(int(kor[0] / 50) * 50, int(kor[1] / 50) * 50, 40, 40)
            pygame.draw.rect(ekraani_pind, (0, 255, 0), ruut)
            pygame.display.flip()
            ruut = pygame.Rect(int(kor[0] / 50) * 50, int(kor[1] / 50) * 50, 40, 40)
            pygame.draw.rect(ekraani_pind, color, ruut)
            x=int((kor[0]-700)/50)+1
            y=int((kor[1]-100)/50)+1
            if vastaselaevad[y][x]=="l":
                vastaselaevad[y][x]="x"
                print("Põhjas")
                ruut = pygame.Rect(int(kor[0] / 50) * 50, int(kor[1] / 50) * 50, 40, 40)
                pygame.draw.rect(ekraani_pind, (255,0,0), ruut)
                pygame.display.flip()
                pohjas += 1
                if(pohjas == 21):
                    print("Mäng läbi")
                    #pygame.quit()
                    break
            elif vastaselaevad[y][x]==" ":
                vastaselaevad[y][x]="o"
                print(random.choice(mooda))
                ruut = pygame.Rect(int(kor[0] / 50) * 50, int(kor[1] / 50) * 50, 40, 40)
                pygame.draw.rect(ekraani_pind, (100,100,100), ruut)
                pygame.display.flip()    
            else:
                print("Mitu korda Sa sama ruutu pommitad?")
                
            #print(x,y,vastaselaevad[y][x])
        
    if event.type == pygame.QUIT:
        break

pygame.quit()
