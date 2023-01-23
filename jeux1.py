from random import randrange
nonb_o=randrange(1,10)
chans =4
genyen =False
nonb_c=int(input("Antre yon nonb ant 1 a 10: \n"))
if nonb_c == nonb_o:
    print("Bravo, ou genyen. Nonb la se byen " ,nonb_o, "\n")
while not genyen and chans != 0:
    if nonb_c < nonb_o:
        nonb_c=int(input("Sa ou antre a twò piti, antre yon nonb: \n"))
    elif nonb_c > nonb_o:
        nonb_c=int(input("Sa ou antre a twò gran, antre yon nonb: \n"))
    else:
        genyen = True
        break
    chans-=1
if genyen:
    print("Bravo, ou genyen. Nonb la se byen " ,nonb_o, "\n")
if chans == 0:
    print("Dezole, ou itilize tout chans ou yo. Nonb ou te dwe devine a se " ,nonb_o, "\n")
