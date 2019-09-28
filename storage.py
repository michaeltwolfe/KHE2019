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
            ID = Item.ID
        )      

    session.add(NewOnId)
    session.commit()

def AddOffId(ZoneName, OffId, OutletName):
    OutletUpdate = session.query(Outlet).filter(Outlet.name == OutletName)
    OutletUpdate.offCode = OffId

    session.commit()


"""""

Other shit

"""""


def GetZones():
    return session.query(Zone.name).all()