import random as ran


CardsPlayer1 = []
CardsPlayer2 = []

CardsDealer1 = []
CardsDealer2 = []

#Function that draws a random card
def Draw():
    Cardset = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    Card = ran.choice(Cardset)
    return Card
#A Simulation of what the dealer in a real game would do (I think this is what they do, if not they are cheating (I guess))
def Dealer():
    #A Loop which runs as long as the dealer has a score under 17
    Under16 = True
    while Under16 == True:
        Card = Draw()
        #There are two lists one for the ace as 1 and one for the ace as 11
        CardsDealer2.append(Card)
        if Card == 11:
            CardsDealer1.append(1)
        else:
            CardsDealer1.append(Card)
        #If the score is over 16 this ends the loop
        if (sum(CardsDealer2) > 16 and sum(CardsDealer2) <= 21) or sum(CardsDealer1) > 16:
            Under16 = False
    #This if statemants returns the correct score and print a little info-text
    if sum(CardsDealer1) and sum(CardsDealer2) > 21:
        print(f"Dealer got busted!")
        return 0, 100
    if sum(CardsDealer1) == 21 and len(CardsDealer1) == 2:
        print("The dealer got a Blackjack")
        return "Blackjack", 0
    if sum(CardsDealer1) == sum(CardsDealer2):
        print(f"The dealer has {sum(CardsDealer1)}")
        return sum(CardsDealer1), len(CardsDealer1)
    else:
        if sum(CardsDealer2) > 21:
            print(f"The dealer has {sum(CardsDealer1)}")
            return sum(CardsDealer1), len(CardsDealer1)
        else:
            print(f"The dealer has {sum(CardsDealer2)}")
            return sum(CardsDealer2), len(CardsDealer1)

#This function defins the actions of the player
def Player():
    #One Draw funtion, so that you draw two cards at the beginning
    Card = Draw()
    CardsPlayer2.append(Card)
    if Card == 11:
        CardsPlayer1.append(1)
    else:
        CardsPlayer1.append(Card)
    #A while loop which runs as long the player hits
    while True:
        Card = Draw()
        CardsPlayer2.append(Card)
        if Card == 11:
            CardsPlayer1.append(1)
        else:
            CardsPlayer1.append(Card)
        #The function ends automatically if you either draw a Blackjack or you go over 21
        if sum(CardsPlayer1) == 21 and len(CardsPlayer1) == 2:
            print("Blackjack!")
            return "Blackjack"
        if sum(CardsPlayer1) > 21:
            print(f"Bust! You had {sum(CardsPlayer1)} points")
            return 0, 100
        #This shows your score (or scores if you got an ace)
        if (sum(CardsPlayer1) == sum(CardsPlayer2)) or sum(CardsPlayer2) > 21:
            print(f"You have {sum(CardsPlayer1)} points")
        else:
            print(f"You have {sum(CardsPlayer1)} or {sum(CardsPlayer2)} points")
        #Here the player can decide if he or she will hit or stand
        hitstand = input("hit oder stand? ")
        if hitstand == "hit":
            continue
        elif hitstand == "stand":
            if sum(CardsPlayer2) > sum(CardsPlayer1) and sum(CardsPlayer2) > 21:
                return sum(CardsPlayer2), len(CardsPlayer1)
            else:
                return sum(CardsPlayer1), len(CardsPlayer1)
        #If the player fails to input a valid choice it will be selected randomly  
        else:
            print("You had one job. Since you failed in it, I will leave you no choice and let luck decide.")
            input()
            Random = ran.random
            if Random == 0:
                print("Hit shall it be!!!")
                continue
            else:
                print("Stand shall it be!!!")
                if sum(CardsPlayer2) > sum(CardsPlayer1) and sum(CardsPlayer2) > 21:
                    return sum(CardsPlayer2), len(CardsPlayer1)
                else:
                    return sum(CardsPlayer1), len(CardsPlayer1)   

#A fuction which determinates who has one
def Winner(Player,Plen, Dealer, Dlen):
    if Dealer == Player:
        if Dealer == 0:
            print(f"You and the Dealer had over 21 points")
        elif (Dealer == "Blackjack") or Plen == Dlen:
            print(f"Draw, because both had the same score.")
        elif Plen > Dlen:
            print(f"You win even though you both have the same score, but you have fewer cards.")
        else:
            print(f"The dealer wins even though you both have the same score, but the dealer has fewer cards.")    
    elif Dealer > Player or Dealer == "Blackjack":
        print(f"The dealer wins with {Dealer}")
    else:
        print(f"Good job, you win! You have {Player}")

#The process of the game with input() in between so that it pauses between each step
CardsPlayer, PlayerLenght = Player()
input()
CardsDealer, DealerLenght = Dealer()
input()
Winner(CardsPlayer, PlayerLenght, CardsDealer, DealerLenght)
