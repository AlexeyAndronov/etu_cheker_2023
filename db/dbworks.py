from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import select, and_ ,delete

from db import Abitur, engine, Speciality, Priority, Superlist

def storeAbitur(codes, points):
    with Session(autoflush=False, bind=engine) as db:
        check = select(Abitur).where(Abitur.code == codes)
        if db.scalar(check) == None:
            db.add(Abitur(code=codes, maxpoint = points))
            db.commit()

def storeSpeciality(data):
    Session = sessionmaker(bind=engine)

    with Session() as db:
        None

def getSpecialitys():
    Session = sessionmaker(bind=engine)

    with Session() as db:
        result = db.query(Speciality).all()
    return result

def storePriority(spec, abit_code, value):
    Session = sessionmaker(bind=engine)
    with Session() as db:
        check = select(Priority).where(and_(Priority.abitur_id == abit_code, Priority.speciality_id == spec))
        if db.scalar(check) == None:
            db.add(Priority(abitur_id=abit_code, speciality_id = spec, priority = value ))
            db.commit()


def getAllAbitur(minPoint = 200):
    Session = sessionmaker(bind=engine)
    with Session() as db:
        work = select(Abitur.code, Abitur.maxpoint).where(Abitur.maxpoint>=minPoint).order_by(Abitur.maxpoint.desc())
        result = db.execute (work)
        return result.fetchall()

def getSpecPlaces():
    Session = sessionmaker(bind=engine)
    with Session() as db:
        work = select(Speciality.code, Speciality.max_abitur)
        result = db.execute(work).fetchall()
        return  result

def getPriorityBy(code):
    Session = sessionmaker(bind=engine)
    with Session() as db:
        work = select(Priority.abitur_id, Priority.speciality_id, Priority.priority).where(Priority.abitur_id == code).order_by(Priority.abitur_id, Priority.priority.asc())
        result = db.execute(work).fetchall()
        return result

def createSuperRecord(spec_code, abitur_code, points, pos):
    Session = sessionmaker(bind=engine)
    with Session() as db:
        check = select(Superlist.id).where(Superlist.abitur_id == abitur_code)
        if db.scalar(check) == None:
            db.add(Superlist(spec_id=spec_code, abitur_id=abitur_code, position = pos, points = points ))
            db.commit()


def cleatSuperlist():
    Session = sessionmaker(bind=engine)
    with Session() as db:
        dellist = delete(Superlist)
        db.execute(dellist)
        db.commit()

def clearAbiturs():
    Session = sessionmaker(bind=engine)
    with Session() as db:
        dellist = delete(Abitur)
        db.execute(dellist)
        db.commit()

def clearPriority():
    Session = sessionmaker(bind=engine)
    with Session() as db:
        dellist = delete(Priority)
        db.execute(dellist)
        db.commit()