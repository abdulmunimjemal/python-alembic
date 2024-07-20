from sqlalchemy import create_engine
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker

from models import Student

import os
from dotenv import load_dotenv

load_dotenv()
database_url = os.getenv("DB_URI")

engine = create_engine(database_url)
Session = sessionmaker(bind=engine)

def app():
    with Session() as session:
        session.add_all([
            Student(name="Alice", age=25, note="Alice's notes"),
            Student(name="Bob", age=24, note="Bob's notes"),
            Student(name="Charlie", age=23, note="Charlie's notes"),
        ])
        session.commit()
    
    with engine.connect() as conn:
        stmt = select(Student)
        result = conn.execute(stmt)
        students = result.fetchall()
        print(students)

if __name__ == "__main__":
    app()
