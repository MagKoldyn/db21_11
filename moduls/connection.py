from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql+psycopg2://postgres:123456@localhost:5432/education_db', echo=True,)
# engine = create_engine('postgresql+psycopg2://postgres@localhost:5432/test',echo=True,)


Session_edu = sessionmaker(engine)