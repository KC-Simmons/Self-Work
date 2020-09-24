import matplotlib.pyplot as plt
import pandas as pd
import random

def createResources():
    resources = []
    for i in range(3):
        resources.append('Stone')
        resources.append('Brick')
    for i in range(4):
        resources.append('Sheep')
        resources.append('Wheat')
        resources.append('Wood')
    resources.append('Desert')
    return resources

def createTileNumbers():
    tilenumbers = []
    for i in range(2):
        for j in [3,4,5,6,8,9,10,11]:
            tilenumbers.append(j)
    tilenumbers.append(2)
    tilenumbers.append(12)
    return tilenumbers

#vert 0-53
adjvertdict = {
    0:[3,4],
    1:[4,5],
    2:[5,6],
    3:[0,7],
    4:[0,1,8],
    5:[1,2,9],
    6:[2,10],
    7:[3,11,12],
    8:[4,12,13],
    9:[5,13,14],
    10:[6,14,15],
    11:[7,16],
    12:[7,8,17],
    13:[8,9,18],
    14:[9,10,19],
    15:[10,20],
    16:[11,21,22],
    17:[12,22,23],
    18:[13,23,24],
    19:[14,24,25],
    20:[15,25,26],
    21:[16,27],
    22:[16,17,28],
    23:[17,18,29],
    24:[18,19,30],
    25:[19,20,31],
    26:[20,32],
    27:[21,33],
    28:[22,33,34],
    29:[23,34,35],
    30:[24,35,36],
    31:[25,36,37],
    32:[26,37],
    33:[27,28,38],
    34:[28,29,39],
    35:[29,30,40],
    36:[30,31,41],
    37:[31,32,42],
    38:[33,43],
    39:[34,43,44],
    40:[35,44,45],
    41:[36,45,46],
    42:[37,46],
    43:[38,39,47],
    44:[39,40,48],
    45:[40,41,49],
    46:[41,42,50],
    47:[43,51],
    48:[44,51,52],
    49:[45,52,53],
    50:[46,53],
    51:[47,48],
    52:[48,49],
    53:[49,50]
}
#tiles 1-19
tilevertdict = {
    0:[1],
    1:[2],
    2:[3],
    3:[1],
    4:[1,2],
    5:[2,3],
    6:[3],
    7:[1,4],
    8:[1,2,5],
    9:[2,3,6],
    10:[3,7],
    11:[4],
    12:[1,4,5],
    13:[2,5,6],
    14:[3,6,7],
    15:[7],
    16:[4,8],
    17:[4,5,9],
    18:[5,6,10],
    19:[6,7,11],
    20:[7,12],
    21:[8],
    22:[4,8,9],
    23:[5,9,10],
    24:[6,10,11],
    25:[7,11,12],
    26:[12],
    27:[8],
    28:[8,9,13],
    29:[9,10,14],
    30:[10,11,15],
    31:[11,12,16],
    32:[12],
    33:[8,13],
    34:[9,13,14],
    35:[10,14,15],
    36:[11,15,16],
    37:[12,16],
    38:[13],
    39:[13,14,17],
    40:[14,15,18],
    41:[15,16,19],
    42:[16],
    43:[13,17],
    44:[14,17,18],
    45:[15,18,19],
    46:[16,19],
    47:[17],
    48:[17,18],
    49:[18,19],
    50:[19],
    51:[17],
    52:[18],
    53:[19]
}

DiceRolltoProdDict = {
    0:0,
    2:1,
    3:2,
    4:3,
    5:4,
    6:5,
    8:5,
    9:4,
    10:3,
    11:2,
    12:1
}

class tile(object):
    def __init__(self, tileid, resource, rollnumber):
        self.tileid = tileid
        self.resource = resource
        self.rollnumber = rollnumber

class vertex(object):
    def __init__(self, vertid,adjhex, adjvert,production):
        self.vertid = vertid
        self.adjhex = adjhex
        self.adjvert = adjvert
        self.production = production
        self.isSettled = False
        self.canBeSettled = True

    def settled(self):
        self.canBeSettled = False
        self.isSettled = True

    def adjsettled(self):
        self.canBeSettled = False

class player(object):
    def __init__(self,playerId,totalProductionOverall):
        self.playerId = playerId
        self.totalProduction = totalProductionOverall

def placeAllTiles():
    tileslist = []
    tilenumlist = range(1,20,1)
    for i in tilenumlist:
        if len(tilenumbers) > 1:
            tilenumberchosen = random.randint(0,len(tilenumbers) - 1)
        else:
            tilenumberchosen = 0
        if resources[i-1] == 'Desert':
            tileslist.append(tile(i,resources[i-1],0))
        else:
            tileslist.append(tile(i,resources[i-1],tilenumbers[tilenumberchosen]))
            tileHasBeenRemoved = False
            for j in range(len(tilenumbers)):
                if tilenumbers[j] == tilenumbers[tilenumberchosen] and tileHasBeenRemoved == False:
                    tileHasBeenRemoved = True
                    tileToRemove = j
            tilenumbers.remove(tilenumbers[tileToRemove])
    return tileslist

#Create All Verts
def createVerts(tileslist):
    vertslist = []
    for i in range(0,54,1):
        vertprod = 0
        for j in range(len(tilevertdict[i])):
            whichTilesIdAdj = tilevertdict[i][j]
            for k in range(len(tileslist)):
                if tileslist[k].tileid == whichTilesIdAdj:
                    vertprod += DiceRolltoProdDict[tileslist[k].rollnumber]
        vertslist.append(vertex(i,tilevertdict[i],adjvertdict[i],vertprod))
    return vertslist


def findBestPlacetoSettle(listofvertices):
    bestproduction = 0
    bestprodvertid = 0
    for i in range(len(listofvertices)):
        if listofvertices[i].production >= bestproduction and listofvertices[i].canBeSettled == True:
            bestproduction = listofvertices[i].production
            bestprodvertid = listofvertices[i].vertid
    
    return [bestproduction,bestprodvertid]

def findBestPlaces(vertslist):
    bestplaces = []
    for i in range(8):
        bestplace = findBestPlacetoSettle(vertslist)
        for j in range(len(vertslist)):
            if vertslist[bestplace[1]] == vertslist[j]:
                vertslist[j].settled()
                adjVertSettled = vertslist[j].adjvert
                for k in range(len(adjVertSettled)):
                    for l in range(len(vertslist)):
                        if adjVertSettled[k] == vertslist[l].vertid:
                            vertslist[l].adjsettled()
        bestplaces.append(bestplace)
    return bestplaces


        
pickNumberMat = [[],[],[],[],[],[],[],[]]
numOfTrials = 10000
ProdMat = [[0,0],[1,0],[2,0],[3,0]]
for i in range(numOfTrials):
    resources = createResources()
    tilenumbers = createTileNumbers()
    vertslist = createVerts(placeAllTiles())
    findBestPlacetoSettle(vertslist)
    bestplaceslist = findBestPlaces(vertslist)

    
    p1 = int(bestplaceslist[0][0]) + int(bestplaceslist[7][0])
    p2 = int(bestplaceslist[1][0]) + int(bestplaceslist[6][0])
    p3 = int(bestplaceslist[2][0]) + int(bestplaceslist[5][0])
    p4 = int(bestplaceslist[3][0]) + int(bestplaceslist[4][0])

    ProdMat[0][1] += p1
    ProdMat[1][1] += p2
    ProdMat[2][1] += p3
    ProdMat[3][1] += p4

    for i in range(8):
        pickNumberMat[i].append(int(bestplaceslist[i][0]))

for i in range(4):
    ProdMat[i][1] /= (numOfTrials*2)


print('Production per House Placed')
print(ProdMat)
print('')

numberPickDB = pd.DataFrame({
    '1st Pick': pickNumberMat[0],
    '2nd Pick': pickNumberMat[1],
    '3rd Pick': pickNumberMat[2],
    '4th Pick': pickNumberMat[3],
    '5th Pick': pickNumberMat[4],
    '6th Pick': pickNumberMat[5],
    '7th Pick': pickNumberMat[6],
    '8th Pick': pickNumberMat[7],
})


boxplot = numberPickDB.boxplot()

plt.show()