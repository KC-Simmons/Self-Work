#Initialize Program
import random as rand
import math
import matplotlib.pyplot as plt
import seaborn as sns
import time

start_time = time.time()

sns.set()


valuedict = {6: 'Ace', 5: 'Ten', 4: 'King', 3: 'Queen',2:'Jack', 1: 'Nine'}
suitdict = {4: 'Clubs', 3: 'Spades' , 2: 'Hearts', 1: 'Diamonds'}

def pickacard(cardspicked):
    isalreadypicked = False
    cardcount = 0

    value = rand.randint(1,6)
    suit = rand.randint(1,4)

    for card in cardspicked:
        if [value,suit] == card:
            cardcount += 1

    if cardcount == 2:
        isalreadypicked = True

    if isalreadypicked == False:
        return([value,suit])
    else:
        return('repeat')

def drawahand(howmanycards):
    onehand = []
    while len(onehand) < howmanycards:
        newcard = pickacard(onehand)
        if newcard != 'repeat':
            onehand.append(newcard)
    return onehand

#Create Test Hand
testhand = [[6,2],[6,3],[6,4],[6,2],[6,3],[6,4],[3,1],[3,1],[6,1],[6,1],[1,1],[1,1]]

def ShowHand(handtoshow):
    for i in range(1,5):
        print(suitdict[i])
        for card in handtoshow:
            if card[1] == i:
                print(valuedict[card[0]])
        print('')
    return('')

#Diamonds, Hearts, Spades, Clubs
def countpointsinhand(givenhand):
    onehandpoints = [0,0,0,0]
    for trump in range(1,5):
        #Check 9 in Trump
        for card in givenhand:
            if card[1] == trump and card[0] == 1:
                onehandpoints[trump-1] += 1
        
        #Check Run
        hasjackrun = 0
        hasqueenrun = 0
        haskingrun = 0
        hastenrun = 0
        hasacerun = 0
        for card in givenhand:
            if card[1] == trump and card[0] == 2:
                hasjackrun += 1
            if card[1] == trump and card[0] == 3:
                hasqueenrun += 1
            if card[1] == trump and card[0] == 4:
                haskingrun += 1
            if card[1] == trump and card[0] == 5:
                hastenrun += 1
            if card[1] == trump and card[0] == 6:
                hasacerun += 1
        #Special Case: Double Run
        if hasjackrun == 2 and hasqueenrun == 2 and haskingrun == 2 and hastenrun == 2 and hasacerun == 2:
            onehandpoints[trump-1] += 22
        elif hasjackrun > 0 and hasqueenrun > 0 and haskingrun > 0 and hastenrun > 0 and hasacerun > 0 :
            onehandpoints[trump-1] += 11

        #Check Pinochle
        jackofdiamond = 0
        queenofspade = 0
        for card in givenhand:
            if card == [2,1]:
                jackofdiamond += 1
            if card == [3,3]:
                queenofspade += 1
        onehandpoints[trump-1] += (4*min(jackofdiamond,queenofspade))

        #Aces Around
        acearounddiamond = 0
        acearoundheart = 0
        acearoundclub = 0
        acearoundspade = 0
        for card in givenhand:
            if card == [6,1]:
                acearounddiamond += 1
            if card == [6,2]:
                acearoundheart += 1
            if card == [6,3]:
                acearoundspade += 1
            if card == [6,4]:
                acearoundclub += 1
        onehandpoints[trump-1] += (10*min(min(acearounddiamond,acearoundheart),min(acearoundclub,acearoundspade)))

        #Kings Around
        kingarounddiamond = 0
        kingaroundheart = 0
        kingaroundclub = 0
        kingaroundspade = 0
        for card in givenhand:
            if card == [4,1]:
                kingarounddiamond += 1
            if card == [4,2]:
                kingaroundheart += 1
            if card == [4,3]:
                kingaroundspade += 1
            if card == [4,4]:
                kingaroundclub += 1
        onehandpoints[trump-1] += (8*min(min(kingarounddiamond,kingaroundheart),min(kingaroundclub,kingaroundspade)))

        #Queens Around
        queenarounddiamond = 0
        queenaroundheart = 0
        queenaroundclub = 0
        queenaroundspade = 0
        for card in givenhand:
            if card == [3,1]:
                queenarounddiamond += 1
            if card == [3,2]:
                queenaroundheart += 1
            if card == [3,3]:
                queenaroundspade += 1
            if card == [3,4]:
                queenaroundclub += 1
        onehandpoints[trump-1] += (6*min(min(queenarounddiamond,queenaroundheart),min(queenaroundclub,queenaroundspade)))

        #Jacks Around
        jackarounddiamond = 0
        jackaroundheart = 0
        jackaroundclub = 0
        jackaroundspade = 0
        for card in givenhand:
            if card == [2,1]:
                jackarounddiamond += 1
            if card == [2,2]:
                jackaroundheart += 1
            if card == [2,3]:
                jackaroundspade += 1
            if card == [2,4]:
                jackaroundclub += 1
        onehandpoints[trump-1] += (4*min(min(jackarounddiamond,jackaroundheart),min(jackaroundclub,jackaroundspade)))

        #Marriages
        if trump == 1:
            onehandpoints[trump-1] += 2*(2*min(kingarounddiamond,queenarounddiamond))
            onehandpoints[trump-1] += (2*min(kingaroundheart,queenaroundheart))
            onehandpoints[trump-1] += (2*min(kingaroundspade,queenaroundspade))
            onehandpoints[trump-1] += (2*min(kingaroundclub,queenaroundclub))
        if trump == 2:
            onehandpoints[trump-1] += (2*min(kingarounddiamond,queenarounddiamond))
            onehandpoints[trump-1] += 2*(2*min(kingaroundheart,queenaroundheart))
            onehandpoints[trump-1] += (2*min(kingaroundspade,queenaroundspade))
            onehandpoints[trump-1] += (2*min(kingaroundclub,queenaroundclub))
        if trump == 3:
            onehandpoints[trump-1] += (2*min(kingarounddiamond,queenarounddiamond))
            onehandpoints[trump-1] += (2*min(kingaroundheart,queenaroundheart))
            onehandpoints[trump-1] += 2*(2*min(kingaroundspade,queenaroundspade))
            onehandpoints[trump-1] += (2*min(kingaroundclub,queenaroundclub))
        if trump == 4:
            onehandpoints[trump-1] += (2*min(kingarounddiamond,queenarounddiamond))
            onehandpoints[trump-1] += (2*min(kingaroundheart,queenaroundheart))
            onehandpoints[trump-1] += (2*min(kingaroundspade,queenaroundspade))
            onehandpoints[trump-1] += 2*(2*min(kingaroundclub,queenaroundclub))
    return(onehandpoints)


amountofcardsdealt = 12
amountofhands = 100000
handmaxpointmat = []
handdrawnoutmat = []

for i in range(amountofhands):
    handdrawn = drawahand(amountofcardsdealt)
    handmaxpointmat.append(max(countpointsinhand(handdrawn)))
    if max(countpointsinhand(handdrawn)) >= 35:
        handdrawnoutmat.append(handdrawn)

for i in range(len(handdrawnoutmat)):
    print(max(countpointsinhand(handdrawnoutmat[i])))
    ShowHand(handdrawnoutmat[i])

print('My program took', time.time() - start_time, 'to run')

pinhist = plt.hist(handmaxpointmat, bins = range(max(handmaxpointmat)), density = True)
pinhist = plt.xlabel('Amount of Points')
pinhist = plt.ylabel('Frequency')
pinhist = plt.title('Frequency - 4 Pl Pin - Max Point in Single Hand - 1,000,000 Trials')
plt.show()
