from app.db import Base
from sqlalchemy import Column, Integer, String
# Use validates() function decorate of the sqlalchemy module to validate data before inserting into db
from sqlalchemy.orm import validates
# Use bcrypt package to encrypt passwords
import bcrypt

# Create a salt to hash passwords against
salt = bcrypt.gensalt()

# Create a User class that inherits form the Base class
# Declare properties that the parent Base class will use to make the table
# Use classes from the sqlalchemy module to define the table columns and their data types
# Give options to each column, e.g. nullable=False
class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)

# Use validate_email() method to check if in amail address contains an @
# Assert keyword automatically throws an error if the condition is false, thus preventing the return statement from happening
  @validates('email')
  def validate_email(self, key, email):
    # make sure email address contains @ character
    assert '@' in email

    return email

# User validate_password method to check length of password
# Use assert keyword to throw an error if password is less than 4 characters
# Return an encrypted version of the password if the assert doesn't throw an error
  @validates('password')
  def validate_password(self, key, password):
    assert len(password) > 4

  # encrypt password
    return bcrypt.hashpw(password.encode('utf-8'), salt)

  def verify_password(self, password):
    return bcrypt.checkpw(
      password.encode('utf-8'),
      self.password.encode('utf-8')
    )