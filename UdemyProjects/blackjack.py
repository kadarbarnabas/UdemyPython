import random as r

class PlayerHand():
    
    def __init__(self, card1, card2, bet):
        self.card1 = card1
        self.card2 = card2
        self.chip = bet
        
class DealerHand():
    
    def __init__(self, card1, card2):
        self.dcard1 = card1
        self.dcard2 = card2
        
class GameLogic():
    
    def bust(self, ossz):
        if ossz > 21:
            return False
        else:
            return True
    
    def sum(self, a, b):
        return (a + b)
    
    def pickup(self):
        return r.randint(2, 11)
    
    def ace_rule(self, card, ossz):
        if card == 11 and ossz > 21:
            return 10
        else:
            return 0

while True:
    try: 
        money = int(input("Mennyivel kíván az asztalhoz ülni?: "))
        break
    except TypeError:
        print("Egy számot adjon meg!")
    except ValueError:
        print("Egy számot adjon meg!")
    except UnboundLocalError:
        print("Egy számot adjon meg!")

while True:
    
    print("\n-------------------------------------------\n")
    print(f"Az önnél lévő összeg: {money}")
    
    while True:
        try:
            print("\n-------------------------------------------\n")
            bet1 = int(input("Adja meg a tétet!: "))
            print(f"A betett tét: {bet1}")
            break
        except TypeError:
            print("Egy számot adjon meg!")
        except ValueError:
            print("Egy számot adjon meg!")
        except UnboundLocalError:
            print("Egy számot adjon meg!")
        
    game = GameLogic()
    player = PlayerHand(game.pickup(), game.pickup(), bet1)
    dealer = DealerHand(game.pickup(), game.pickup())
    
    
    possz = game.sum(player.card1, player.card2)
    if possz == 22 and player.card1 == 11:
        possz -= 10
        player.card1 -= 10
    dossz = game.sum(dealer.dcard1, dealer.dcard2)
    if dossz == 22 and dealer.dcard1 == 11:
        dossz -= 10
        dealer.dcard1 -= 10
    
    print("\n-------------------------------------------\n")
    print(f"Az ön kártyáji: {player.card1} és {player.card2} aminek az összege: {possz}")
    print(f"Az osztó első kártyája: {dealer.dcard1}")
    
    while game.bust(possz):
        
        print("\n-------------------------------------------\n")
        hit = input(f"Akar új lapot húzni?(Y / N): ")
        if hit.lower() == 'y':
            drawcard = game.pickup()
            possz += drawcard
            possz -= game.ace_rule(drawcard, possz)
            print(f"A felhúzott kártya: {drawcard} és így az összeg {possz}")
        else:
            print("\n-------------------------------------------\n")
            print(f"Az osztó kártyáji: {dealer.dcard1} és {dealer.dcard2} aminek az összege: {dossz}")
            while possz > dossz:
                newcard = game.pickup()
                dossz += newcard
                dossz -= game.ace_rule(newcard, dossz)
                print(f"Az osztó új kártyája: {newcard} és így az összeg: {dossz}")
                
                if game.bust(dossz):
                    break
                    
        if game.bust(possz) == False:
            print("\n-------------------------------------------\n")
            print(f"Az osztó kártyáji: {dealer.dcard1} és {dealer.dcard2} aminek az összege: {dossz}")
            
        if hit.lower() != 'y':
            break
    
    print("\n-------------------------------------------\n")
    if (dossz > possz and dossz <= 21) or possz > 21:
        print(f"Az osztó nyert! | Az osztós kártyájinak az összege {dossz}")
        money -= bet1
    elif (possz > dossz and possz <=21) or dossz > 21:
        print(f"A játékos nyert! | A játékos kártyájinak az összege {possz}")
        money += bet1 * 2
    elif (dossz == possz) and dossz <=21 and possz <=21:
        print(f"A kör döntetlen | Játékos: {possz} | Osztó: {dossz}")
    
    if money <= 0:
        print("\n-------------------------------------------\n")
        print("Nem tud több játékot játszani!")
        break
    
    print("\n-------------------------------------------\n")  
    nextround = input("Akar új kört játszani?(Y / N): ")
    if nextround.lower() != 'y':
        print("\n-------------------------------------------\n") 
        print(f"A kiszállásnál lévő összeg: {money}")
        break  

    