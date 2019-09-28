import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, DateTime, ForeignKey, CHAR, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://root@localhost/KHE2019")

Base = declarative_base(engine)

class Zone(Base):
    __tablename__ = "Zone"
    __table_args__ = {"autoload": True}

class Outlet(Base):
    __tablename__ = "Outlet"
    __table_args__ = {"autoload": True}

class Weekly(Base):
    __tablename__ = "Weekly"
    __table_args__ = {"autoload": True}

class Daily(Base):
    __tablename__ = "Daily"
    __table_args__ = {"autoload": True}