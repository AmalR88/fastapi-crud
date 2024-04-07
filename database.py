from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQL_ALCHEMY_DATABASE_USERS_URL="sqlite:///./users.db"


#creating engine 
engine = create_engine(
    
     SQL_ALCHEMY_DATABASE_USERS_URL, connect_args={"check_same_thread": False}
)

# Declare a mapping
Base=declarative_base()


# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
