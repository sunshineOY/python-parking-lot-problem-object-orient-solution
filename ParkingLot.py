'''
Created on 2014-11-29

@author: ouyangsiqi
'''
from Constants import Constants
from Space import Space
from Level import Level
class ParkingLot:
    class NoParkingSpaceError(Exception): pass
    '''
    The class is the whole parking lot
    '''
    __levels = []
    __levelCount = 0
    __totalSpaceCount = 0
    __totalEmptySpaceCount = 0

    def __init__(self):
        '''
        Constructor
        '''
        self.__levelCount = int(raw_input("to define the parking lot's level count:"))
        
        for i in range(self.__levelCount):
            spaceCount = int(raw_input("to define the space count in level " + str(i + 1) + " of the parking lot:"))
            spacesOfEachLevel = []
            for j in range(spaceCount):
                spacesOfEachLevel.append(Space())
            self.__levels.append(Level(spacesOfEachLevel))
            self.__totalSpaceCount += spaceCount

        self.__totalEmptySpaceCount = self.__totalSpaceCount;

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

    def showParkingStatus(self):
        for i in range(self.__levelCount):
            print "parking status in level " + str(i + 1) + ":"
            self.__levels[i].showLevelParkingStatus()
            print ""

    def parkTheCar(self):
        '''
        To park the car in the random space of the random level
        '''
        hasSpace = False;
        for i in range(self.__levelCount):
            for j in range(self.__levels[i].getSpaceCount()):
                if not self.__levels[i].getSpaces()[j].checkIfCarParked():
                    self.__levels[i].getSpaces()[j].parkCar()
                    self.__totalEmptySpaceCount -= 1
                    hasSpace = True;
                    return {Constants.levelNumberKey: i + 1, Constants.spaceNumberKey: j + 1}
                else:
                    continue
        if not hasSpace:
            raise self.NoParkingSpaceError, "no empty parking spaces"

    def allowToPark(self):
        '''
        The method to check if the parking lot allow to park
        '''
        return self.__totalEmptySpaceCount > 0
