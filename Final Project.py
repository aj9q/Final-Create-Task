import random
import math

gameName = str(input("What is the name of the game being played? "))
#print (gameName)
players = []
matchups = {}
numMatches = 0
roundNumber = 1
i = 0

while i != 'N':
    players.append(input("Enter a player's name. "))
    print (players)
    i = str(input('Are there more players? (Y/N) '))
numPlayers = int(len(players))
print(numPlayers, "players in the tournament!", '\n')
numMatches = math.trunc(numPlayers ** 1/2)
 
def matchUp(players, numMatches, numPlayers):
    g = 0
#    print (numMatches, "matches in round", roundNumber)
    if numMatches != numPlayers / 2:
        byPlayer = random.choice(players)
        players.remove(byPlayer)
#        print(players)
        print ("Free round given to", byPlayer, '\n')
        numPlayers = len(players)
    while g != (len(players) / 2) + g:
#        print ('Number of players =', len(players))
        n = 0
        buffer = (random.sample(players,2))
#        print (buffer)
        matchups.update({g:buffer})
        while n != len(buffer):
            players.remove(buffer[n])
            n += 1
#        print('Matchups =',matchups)
#        print('Players =', players)
        g += 1
    print ("Round", roundNumber, "Matches are: ")
    print ('_____________________________', '\n')
#    print (matchups)
#    print('g value is:', g)
    r = 0
    if 'byPlayer' in locals():
        matchups.update({g:byPlayer})
        while r != g + 1:
            print (matchups[r])
#            print (r)
            r += 1
    else:
        while r != g:
            print (matchups[r])
#            print (r)
            r += 1

#print (players)
#print (len(players))
print (gameName, 'tournament begins now!')
matchUp(players, numMatches, numPlayers)

