import os

from sqlalchemy import Column, String, Integer, ForeignKey, DECIMAL, Boolean, Text, Float
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, reconstructor
from sqlalchemy.types import ARRAY

import settings
Base = declarative_base()


class BaseModel(object):
    id = Column(Integer)

class Country(Base, BaseModel):
    __tablename__ = 'countries'
    name = Column(String)

class Disease(Base, BaseModel):
    __tablename__ = 'diseases'
    name = Column(String)

class GeoLocation(Base, BaseModel):
    __tablename__ = 'geo_locations'
    coord_precision = Column(DECIMAL)
    x_coord = Column(DECIMAL)
    y_coord = Column(DECIMAL)
    address = Column(String)
    zipcode = Column(String)
    country_id = Column(Integer, ForeignKey(Country.id))


class Species(Base, BaseModel):
    __tablename__ = 'species'
    name = Column(String)


class ProductionType(Base, BaseModel):
    __tablename__ = 'production_types'
    name = Column(String)


class Establishment(Base, BaseModel):
    __tablename__ = 'establishments'
    geo_location_id = Column(Integer, ForeignKey(GeoLocation.id))
    production_type_id = Column(Integer, ForeignKey(ProductionType.id))


class SubUnit(Base, BaseModel):
    __tablename__ = 'sub_units'
    establishment_id = Column(Integer, ForeignKey(Establishment.id))
    geo_location_id = Column(Integer, ForeignKey(GeoLocation.id))
    production_type_id = Column(Integer, ForeignKey(ProductionType.id))
    species_id = Column(Integer, ForeignKey(Species.id))
    actual_number = Column(Integer)
    capacity = Column(Integer)


class Animal(Base, BaseModel):
    __tablename__ = 'animals'
    species_id = Column(Integer, ForeignKey(Species.id))
    production_type_id = Column(Integer, ForeignKey(ProductionType.id))
    sub_unit_id = Column(Integer, ForeignKey(SubUnit.id))
    establishment_id = Column(Integer, ForeignKey(Establishment.id))
    birth_establishment_id = Column(Integer, ForeignKey(Establishment.id))
    birth_sub_unit_id = Column(Integer, ForeignKey(SubUnit.id))
    birth_country_id = Column(Integer, ForeignKey(Country.id))
    sex = Column(Integer)
    birth_date = Column(DateTime)
    mother_animal_id = Column(Integer, ForeignKey(Animal.id))


class DiseaseDetection(Base, BaseModel):
    __tablename__ = 'disease_detections'
    geo_location_id = Column(Integer, ForeignKey(GeoLocation.id))
    disease_id = Column(Integer, ForeignKey(Disease.id))
    species_id = Column(Integer, ForeignKey(Species.id))
    production_type_id = Column(Integer, ForeignKey(ProductionType.id))
    outbreak_type = Column(String)
    num_susceptible = Column(Integer)
    num_affected = Column(Integer)
    num_killed = Column(Integer)
    num_destroyed = Column(Integer)
    kg_destroyed = Column(String)
    suspicion_date = Column(DateTime)
    confirmation_date = Column(DateTime)


class MonitoringData(Base, BaseModel):
    __tablename__ = 'monitoring_datas'
    animal_id = Column(Integer, ForeignKey(Animal.id))
    sub_unit_id = Column(Integer, ForeignKey(SubUnit.id))
    establishment_id = Column(Integer, ForeignKey(Establishment.id))
    disease_detection_id = Column(Integer, ForeignKey(DiseaseDetection.id))