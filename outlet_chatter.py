#Created by: Mike Wolfe

import subprocess
import sys

class OutletChatter:

    def __init__(self):
        pass

    #used for setting up a new outlet
    def GetOnId(self):
        with open("IdLog.txt") as File:
            Data = File.readlines()

        return Data[-1]

    def GetOffId(self):
        with open("IdLog.txt") as File:
            Data = File.readlines()

        return Data[-1]
    
    #on/off duh!
    def TurnOnOutlet(self, OutletId):
        pass

    def TurnOffOutlet(self, OutletId):
        pass