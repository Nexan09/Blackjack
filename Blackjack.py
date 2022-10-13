import random as ran

CardsPlayer1 = []
CardsPlayer2 = []

CardsDealer1 = []
CardsDealer2 = []
print("Wiär nämmed jetzt eifach mal a, dass mer mit unändlich vielä Sets spieled, will ich ha ÄCHT KEI BOCK ä chartä Limitä z implentiärä")
def Ziehen():
    Cardset = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    Card = ran.choices(Cardset)
    return sum(Card)

def Dealer():
    Unter16 = True
    while Unter16 == True:
        Card = Ziehen()
        CardsDealer2.append(Card)
        if Card == 11:
            CardsDealer1.append(1)
        else:
            CardsDealer1.append(Card)
        if (sum(CardsDealer2) > 16 and sum(CardsDealer2) <= 21) or sum(CardsDealer1) > 16:
            Unter16 = False
    if sum(CardsDealer1) and sum(CardsDealer2) > 21:
        print(f"Dealer Überschossen!")
        return 0, 100
    if sum(CardsDealer1) == 21 and len(CardsDealer1) == 2:
        print("Dealer hat Blackjack")
        return "Blackjack", 0
    if sum(CardsDealer1) == sum(CardsDealer2):
        print(f"Dealer hat {sum(CardsDealer1)}")
        return sum(CardsDealer1), len(CardsDealer1)
    else:
        if sum(CardsDealer2) > 21:
            print(f"Dealer hat {sum(CardsDealer1)}")
            return sum(CardsDealer1), len(CardsDealer1)
        else:
            print(f"Dealer hat {sum(CardsDealer2)}")
            return sum(CardsDealer2), len(CardsDealer1)
def Spieler():
    Card = Ziehen()
    CardsPlayer2.append(Card)
    if Card == 11:
        CardsPlayer1.append(1)
    else:
        CardsPlayer1.append(Card)
    while True:
        Card = Ziehen()
        CardsPlayer2.append(Card)
        if Card == 11:
            CardsPlayer1.append(1)
        else:
            CardsPlayer1.append(Card)
        if sum(CardsPlayer1) == 21 and len(CardsPlayer1) == 2:
            print("Blackjack!")
            return "Blackjack"
        if sum(CardsPlayer1) > 21:
            print(f"Du hast dich Überschossen. Du hattest {sum(CardsPlayer1)} Punkte")
            return 0, 100
        if (sum(CardsPlayer1) == sum(CardsPlayer2)) or sum(CardsPlayer2) > 21:
            print(f"Du hast {sum(CardsPlayer1)} Punkte")
        else:
            print(f"Du hast {sum(CardsPlayer1)} oder {sum(CardsPlayer2)} Punkte")
        hitstand = input("hit oder stand? ")
        if hitstand == "hit":
            continue
        elif hitstand == "stand":
            if sum(CardsPlayer2) > sum(CardsPlayer1) and sum(CardsPlayer2) > 21:
                return sum(CardsPlayer2), len(CardsPlayer1)
            else:
                return sum(CardsPlayer1), len(CardsPlayer1)
        else:
            print("Boy, dass ist keine Auswahlmöglichkeit. Darum hit ich dir ins face oder so")
            continue

def Gewinner(Player,Plen, Dealer, Dlen):
    if Dealer == Player:
        if Dealer == 0:
            print(f"Bravo, ihr habt euch beide Überschossen, Glück gehabt")
        elif (Dealer == "Blackjack") or Plen == Dlen:
            print(f"Unentschieden, da beide {Dealer} hatten.")
        elif Plen > Dlen:
            print(f"Du gewinnst ob wohl ihr beide die Gleiche Punktzahl, jedoch du es mit weniger Karten hattes")
        else:
            print(f"Der Dealer gewinnt ob wohl ihr beide die Gleiche Punktzahl, jedoch er es mit weniger Karten hatte")    
    elif Dealer > Player or Dealer == "Blackjack":
        print(f"Der Dealer gewinnt mit {Dealer}")
    else:
        print(f"Bravo, du gewinnst! Du hattest {Player}")

CardsPlayer, PlayerLenght = Spieler()
CardsDealer, DealerLenght = Dealer()
Gewinner(CardsPlayer, PlayerLenght, CardsDealer, DealerLenght)
