from sqlalchemy import Column, String, Integer, ForeignKey, DECIMAL, Boolean, Text, Float,BigInteger
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class BaseModel:
    id = Column(Integer,primary_key=True)

class countries(Base, BaseModel):
    __tablename__ = 'countries'
    name = Column(String(50))

class diseases(Base, BaseModel):
    __tablename__ = 'diseases'
    name = Column(String(50))

class geo_locations(Base, BaseModel):
    __tablename__ = 'geo_locations'
    coord_precision = Column(DECIMAL)
    x_coord = Column(DECIMAL)
    y_coord = Column(DECIMAL)
    address = Column(String(50))
    zipcode = Column(String(50))
    country_id = Column(Integer, ForeignKey(countries.id))


class species(Base, BaseModel):
    __tablename__ = 'species'
    name = Column(String(50))


class production_types(Base, BaseModel):
    __tablename__ = 'production_types'
    name = Column(String(50))


class establishments(Base, BaseModel):
    __tablename__ = 'establishments'
    geo_location_id = Column(Integer, ForeignKey(geo_locations.id))
    production_type_id = Column(Integer, ForeignKey(production_types.id))


class sub_units(Base, BaseModel):
    __tablename__ = 'sub_units'
    establishment_id = Column(Integer, ForeignKey(establishments.id))
    geo_location_id = Column(Integer, ForeignKey(geo_locations.id))
    production_type_id = Column(Integer, ForeignKey(production_types.id))
    species_id = Column(Integer, ForeignKey(species.id))
    actual_number = Column(Integer)
    capacity = Column(Integer)


class animals(Base, BaseModel):
    __tablename__ = 'animals'
    species_id = Column(Integer)
    production_type_id = Column(Integer)
    sub_unit_id = Column(Integer)
    establishment_id = Column(Integer)
    birth_establishment_id = Column(Integer)
    birth_sub_unit_id = Column(Integer)
    birth_country_id = Column(Integer)
    sex = Column(Integer)
    birth_date = Column(DateTime)
    mother_animal_id = Column(Integer)


class disease_detections(Base, BaseModel):
    __tablename__ = 'disease_detections'
    geo_location_id = Column(Integer, ForeignKey(geo_locations.id))
    disease_id = Column(Integer, ForeignKey(diseases.id))
    species_id = Column(Integer, ForeignKey(species.id))
    production_type_id = Column(Integer, ForeignKey(production_types.id))
    outbreak_type = Column(String(50))
    num_susceptible = Column(Integer)
    num_affected = Column(Integer)
    num_killed = Column(Integer)
    num_destroyed = Column(Integer)
    kg_destroyed = Column(String(50))
    suspicion_date = Column(DateTime)
    confirmation_date = Column(DateTime)


class monitoring_datas(Base, BaseModel):
    __tablename__ = 'monitoring_datas'
    animal_id = Column(Integer, ForeignKey(animals.id))
    sub_unit_id = Column(Integer, ForeignKey(sub_units.id))
    establishment_id = Column(Integer, ForeignKey(establishments.id))
    disease_detection_id = Column(Integer, ForeignKey(disease_detections.id))
#-------END TABLES CLASS-------
#Function get tables information
def get_list_tables():
    return list(Base.metadata.tables.keys())
def get_list_columns(object):
    return list(object.__table__.c.keys())
def get_table_object(table):
    klass = globals()[table]
    object = klass()
    return object
def get_list_columns_in_table(table_name):
    return  list(Base.metadata.tables[table_name].columns.keys())