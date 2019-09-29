#Created by: Mike Wolfe

import sys
import os

class OutletChatter:

    def __init__(self):
        pass

    #used for setting up a new outlet
    def GetOnId(self):
        with open("IdLog.txt") as File:
            Data = File.readlines()
            
        Data = Data[-1].split(' ')
        return Data[1]

    def GetOffId(self):
        with open("IdLog.txt") as File:
            Data = File.readlines()

        Data = Data[-1].split(' ')
        return Data[1]
    
    #on/off duh!
    def TurnOnOutlet(self, OutletId):
        os.system("/home/pi/rfoutlet/codesend " + str(OutletId) + " -1 200~")

    def TurnOffOutlet(self, OutletId):
        os.system("/home/pi/rfoutlet/codesend " + str(OutletId) + " -1 200~")