'''
Created on 2014-11-29

@author: ouyangsiqi
'''
from ParkingLot import ParkingLot


parkingLot = ParkingLot()

carsCount = int(raw_input("input the count of the cars waiting to park:"))
while parkingLot.allowToPark() and carsCount > 0:
    parkingLot.parkTheCar()
    carsCount -= 1
    if carsCount == 0:
        break;
else:
    print "the parking lot is full, the cars after NO." + str(parkingLot.getTotalSpaceCount()) + " shall be waiting for empty space."

parkingLot.showParkingStatus()