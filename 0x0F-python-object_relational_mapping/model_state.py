#!/usr/bin/python3
"""Module to define the State class and Base instance."""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


Base = declarative_base()

class State(Base):
    """Class definition of a State."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Connect to the MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://username:password@localhost:3306/db_name', pool_pre_ping=True)

    # Import the class definition before calling create_all
    from your_file_name import State

    # Create the table
    Base.metadata.create_all(engine)

    # Example of using the State class
    session = Session(engine)
    
    # Add a new state
    new_state = State(name='New State')
    session.add(new_state)
    session.commit()

    # Query and print all states
    states = session.query(State).all()
    for state in states:
        print(state.id, state.name)

    # Close the session
    session.close()
