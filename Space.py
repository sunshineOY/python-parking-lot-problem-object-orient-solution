'''
Created on 2014-11-29

@author: ouyangsiqi
'''

class Space:
    '''
    The class is the spaces to park the cars in each level of the parking lot
    '''
    __isCarParked = False

    def __init__(self):
        '''
        Constructor
        '''
        self.__isCarParked = False

    def parkCar(self):
        '''
        The method is to set the park-car-flag to true to execute the action of parking
        '''
        self.__isCarParked = True

    def checkIfCarParked(self):
        '''
        The method is to check if the space has a car parking here
        '''
        return self.__isCarParked;