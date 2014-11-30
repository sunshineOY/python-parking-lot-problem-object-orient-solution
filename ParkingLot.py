'''
Created on 2014-11-29

@author: ouyangsiqi
'''
from Space import Space
from Level import Level
from CardReader import CardReader
from Card import Card
class ParkingLot:
    class NoParkingSpaceError(Exception): pass
    '''
    The class is the whole parking lot
    '''
    __levels = []
    __cardReader = None
    __levelCount = 0
    __totalSpaceCount = 0
    __totalEmptySpaceCount = 0
    __spaceCountEachLevel = 0

    def __init__(self):
        '''
        Constructor
        '''
        self.__levelCount = int(raw_input("to define the parking lot's level count:"))
        cards = []
        for i in range(self.__levelCount):
            levelId = i + 1
            self.__spaceCountEachLevel = int(raw_input("to define the space count in level " + str(levelId) + " of the parking lot:"))
            spacesOfEachLevel = []
            for j in range(self.__spaceCountEachLevel):
                spaceId = i * self.__spaceCountEachLevel + j + 1
                spacesOfEachLevel.append(Space(spaceId))
                cards.append(Card(spaceId, levelId, spaceId))
            self.__levels.append(Level(spacesOfEachLevel, levelId))
            self.__totalSpaceCount += self.__spaceCountEachLevel

        self.__cardReader = CardReader(cards)

    def showParkingStatus(self):
        '''
        The method to show the parking status of the parking lot
        '''
        for i in range(self.__levelCount):
            print "parking status in level " + str(i + 1) + ":"
            self.__levels[i].showLevelParkingStatus()
            print ""

    def parkTheCar(self):
        '''
        To park the car in the position as the card says
        '''
        card = self.__cardReader.pickCardForParking()
        levelId = card.getLevelId()
        spaceId = card.getSpaceId()
        self.__levels[levelId - 1].getSpaces()[spaceId % self.__spaceCountEachLevel - 1].parkCar()
        return card

    def leaveTheCar(self, card):
        '''
        The car leaves off the space
        '''
        levelId = card.getLevelId()
        spaceId = card.getSpaceId()
        self.__levels[levelId - 1].getSpaces()[spaceId % self.__spaceCountEachLevel - 1].leaveCar()
        self.__cardReader.returnTheCard(card)

    def allowToPark(self):
        '''
        The method to check if the parking lot allow to park
        '''
        return self.__cardReader.getLeftCardCount() > 0

    def getLevelCount(self):
        '''
        The method to get the level count of the parking lot
        '''
        return self.__levelCount

    def getLevels(self):
        '''
        The method to get the levels
        '''
        return self.__levels

    def getTotalSpaceCount(self):
        '''
        The method to get the total spaces count
        '''
        return self.__totalSpaceCount

    def getTotalEmptySpaceCount(self):
        '''
        The method to get the total empty spaces count
        '''
        return self.__cardReader.getLeftCardCount()

    def getCardReader(self):
        '''
        The method to get the card reader
        '''
        return self.__cardReader