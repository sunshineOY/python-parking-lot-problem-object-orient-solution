'''
Created on 2014-11-30

@author: ouyangsiqi
'''

class CardReader:
    '''
    This class is the card reader which gives car-owners card for parking
    '''
    __cards = []
    __cardCount = 0
    __leftCardCount = 0


    def __init__(self, cards):
        '''
        Constructor
        '''
        self.__cards = cards
        self.__cardCount = len(cards)
        self.__leftCardCount = len(cards)

    def getCardCount(self):
        '''
        The method to get the card count
        '''
        return self.__cardCount

    def getCards(self):
        '''
        The method to get all the cards
        '''
        return self.__cards

    def getLeftCardCount(self):
        '''
        The method to get the left cards count
        '''
        return self.__leftCardCount

    def pickCardForParking(self):
        '''
        The method to get a card for parking the car
        '''
        self.__leftCardCount -= 1
        return self.__cards.pop(0)

    def returnTheCard(self, card):
        '''
        The method to return the card
        '''
        self.__leftCardCount += 1
        self.__cards.insert(card.getCardId() - 1, card)