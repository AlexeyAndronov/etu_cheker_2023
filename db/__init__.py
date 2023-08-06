from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.ext.automap import automap_base

connection = "postgresql://postgres:postgres@localhost:5432/etu"
engine = create_engine(connection, client_encoding='utf8')
metadata = MetaData()
metadata.reflect(engine, only=['abitur','priority','speciality', 'superlist'])

Base = automap_base(metadata=metadata)

Base.prepare()

Abitur = Base.classes.abitur
Speciality = Base.classes.speciality
Priority = Base.classes.priority
Superlist = Base.classes.superlist