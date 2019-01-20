from random import randint
import pygame


def trsfdga():
    mitulaeva = 8
    laevadearv = 0
    kohad = [[" " for j in range(12)] for i in range(12)]
    # print(kohad)
    while laevadearv < mitulaeva:
        algusx = randint(1, 10)
        algusy = randint(1, 10)
        # Olgu suun 0 - paremale, 1 alla
        if algusx > 8 and algusy > 8:
            suund = -1
        elif algusx > 8 and algusy < 9:
            suund = 1
        elif algusy > 8 and algusx < 9:
            suund = 0
        else:
            suund = randint(0, 1)
        laev = True

        if suund == -1:
            laev = False
        if suund == 0:
            for x in range(algusx, algusx + 3):
                if kohad[algusy][x] == "l" or kohad[algusy - 1][x] == "l" or kohad[algusy + 1][x] == "l":
                    laev = False
            if (kohad[algusy][algusx - 1] == "l" or kohad[algusy][algusx + 3] == "l"):
                laev = False
        if suund == 1:
            for y in range(algusy, algusy + 3):
                if kohad[y][algusx] == "l" or kohad[y][algusx - 1] == "l" or kohad[y][algusx + 1] == "l":
                    laev = False
            if kohad[algusy - 1][algusx] == "l" or kohad[algusy + 3][algusx] == "l":
                laev = False

        if laev == True:
            laevadearv += 1
            for a in range(0, 3):
                if suund == 0:
                    kohad[algusy][algusx + a] = "l"
                else:
                    kohad[algusy + a][algusx] = "l"
    # end while

    #print("vastaselaevad")
    for n in range(12):
        vlaevad = kohad
        #print(n, " - ", vlaevad[n])
    return vlaevad