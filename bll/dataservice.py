from sqlalchemy import func

from root.dal.db import engine, Base, Session
from sqlalchemy.orm.attributes import InstrumentedAttribute

Base.metadata.create_all(engine)

session = Session()


def get_data(class_name):
    return session.query(class_name).all()


def get_data_by_id(class_name, gradebook_number):
    return session.query(class_name).filter_by(gradebook_number = int(gradebook_number)).first()


def insert_data(data):
    session.add(data)


def delete_data(class_name,id):
    user = session.query(class_name).filter_by(gradebook_number = id).first()
    session.delete(user)


def update_data(obj, class_name):
    mapped_values = {}
    for item in class_name.__dict__.items():
        field_name = item[0]
        field_type = item[1]
        is_column = isinstance(field_type, InstrumentedAttribute)
        if is_column:
            mapped_values[field_name] = getattr(obj, field_name)

    session.query(class_name).filter_by(gradebook_number = obj.gradebook_number).update(mapped_values)


def req1(cl1, cl2, cl3):
    res = session.query(cl1.first_name, func.count(cl3.name))\
        .select_from(cl1)\
        .join(cl2)\
        .join(cl3)\
        .group_by(cl1.first_name).all()
    return res


def req2(cl1, cl2, cl3):
    res = session.query(cl2.id, cl1.first_name, cl1.second_name, cl3.name) \
        .select_from(cl1) \
        .join(cl2) \
        .join(cl3) \
        .all()
    return res


def req3(cl1, cl2, cl3):
    res = session.query(cl3.name, func.count(cl3.name)) \
        .select_from(cl1) \
        .join(cl2) \
        .join(cl3) \
        .group_by(cl3.name).all()
    return res


def save():
    session.commit()


def get_data_by_init(class_name, id):
    return session.query(class_name).filter_by(initalization_num = int(id)).first()



def delete_data_init(class_name,initalization_num):
    user = session.query(class_name).filter_by(initalization_num = initalization_num).first()
    session.delete(user)