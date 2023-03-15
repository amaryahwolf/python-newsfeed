from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# the getenv() function is part of python's built-in os module but bc we used a .env to fake the environment variable, we need to first call load_dotenv() from the python-dotenv module
load_dotenv()

# connect to database using env variable
# engine variable manages the overall connection to the db
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# Session variable generates temporary connections for performing CRUD operations
Session = sessionmaker(bind=engine)
# Base class variable helps us map the models to real MySQL tables
Base = declarative_base()