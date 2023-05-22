def display(tabla):
    for i in range(len(tabla)):
        for j in range(len(tabla[i])):
            if j == 2: 
                print(tabla[i][j], end=' ')
            else:
                print(tabla[i][j], end='|')
        print()  

def ifwin(map):
    same = True
    for i in range(len(map)):
        if (map[i][0] == map[i][1] and map[i][0] == map[i][2]) and map[i][0] != '-':
            same = False
            break
        elif (map[0][i] == map[1][i] and map[0][i] == map[2][i]) and map[0][i] != '-':
            same = False
            break
        elif (map[0][0] == map[1][1] and map[0][0] == map[2][2]) and map[1][1] != '-':
            same = False
            break
        elif (map[0][2] == map[1][1] and map[0][2] == map[2][0]) and map[1][1] != '-':
            same = False
            break
        else:
            same = True
        
    return same
        
while True:
    tabla = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]   
    
    i = 0
    jatek = True
    while jatek:
        
        if i % 2 == 0:
            jatekos = 'X'
            besor = int(input(f"{jatekos} adja meg a kívánt sor: "))
            beoszlop = int(input(f"{jatekos} adja meg a kívánt oszlopot: "))
        else:
            jatekos = 'O'
            besor = int(input(f"{jatekos} adja meg a kívánt sor: "))
            beoszlop = int(input(f"{jatekos} adja meg a kívánt oszlopot: "))
        
        if besor > 3 or beoszlop > 3:
            print("Egy és Három közötti számot adjon meg")
            
        else:
            if tabla[besor - 1][beoszlop - 1] != 'X' and tabla[besor - 1][beoszlop - 1] != 'O':
                tabla[besor - 1][beoszlop - 1] = jatekos
                i += 1
                display(tabla)
            else:
                print("Adjon meg egy másik kordinátát!")
        
        jatek = ifwin(tabla)
        
        if i == 9:
            print("A játék döntetlen")
            break

    if jatek == False:
        print(f"Az {jatekos} játékos nyert")
        
    ujjatek = input("Akar -e egy új játékot játszani?(Y / N): ").upper()
    
    if ujjatek == 'N':
        break