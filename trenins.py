def rezultats(sk1, sk2):
    if sk1<6 and sk2<6:
        rez = sk1*sk2
    else:
        rez = sk1+sk2

    return rez

for skaitlis in range(1, 11, 2):        #range - funkcija, kas skaita skaitļus
    for otrs in range(2, 11, 2):
        print("pirmais skaitlis:", skaitlis,"otrais skaitlis:", otrs, "rezultāts: ", rezultats(skaitlis, otrs))


def zvaigznites1(skaits):
    for rindasNr in range(1, skaits+1):
        for zvaigzne in range(rindasNr):
            print("*", end="")
        print("")

def zvaigznites2(skaits):
    for rindasNr in range(1, skaits+1):
        print("*"*rindasNr)


zvaigznites1(7)