from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_model import *

engine = create_engine("mysql://root@localhost/KHE2019")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def AddZone(ZoneName):
    NewZone = Zone(
        state = 0,
        name = ZoneName
    )

    session.add(NewZone)
    session.commit()

def AddOnId(ZoneName, OnId, OutletName):
    ZoneId = session.query(Zone).filter(Zone.name == ZoneName)
    
    for Item in ZoneId:
        NewOnId = Outlet(
            name = OutletName,
            onCode = OnId,
            offCode = 0,
            ID = Item.ID
        )      

    session.add(NewOnId)
    session.commit()

def AddOffId(ZoneName, OffId, OutletName):
    session.query(Outlet).filter(Outlet.name == OutletName).update({'offCode': OffId})

    session.commit()


"""""

Other shit

"""""


def GetZones():
    ZonesList = []

    Zones = session.query(Zone).all()

    for Item in Zones:
        ZonesList.append(Item.name)

    return ZonesList


def GetLandingPageInformation():
    ZonesList = GetZones()
    CompleteZoneList = []

    for Item in ZonesList:
        OutletsList = []
        ZoneId = session.query(Zone).filter(Zone.name == Item)

        for Id in ZoneId:
            Outlets = session.query(Outlet).filter(Outlet.ID == Id.ID)

        for Names in Outlets:
                OutletsList.append(Names.name)

        ZoneDict = {
            "zone": Item,
            "zoneOutlets": OutletsList
        }

        CompleteZoneList.append(ZoneDict)
        
    return ZoneDict
