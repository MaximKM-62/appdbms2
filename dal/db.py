from root.dal.credentials import BASE, USERNAME, PASSWORD, HOST, PORT, DATABASE

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = '{base}://{user}:{pw}@{host}:{port}/{db}'.format(base= BASE,user=USERNAME,pw=PASSWORD,host=HOST,port=PORT,db=DATABASE)

engine = create_engine(db_string)
Session = sessionmaker(bind=engine)

Base = declarative_base()