from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, func, MetaData

Base = declarative_base(metadata=MetaData(schema='myschema'))
metadata = Base.metadata

class Student(Base):
    __tablename__ = 'students'
    # __table_args__ = {'schema': 'myschema'}
    
    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    note = Column(String(255))
    created_at = Column(DateTime, default=func.now())
    
    def __repr__(self):
        return f'<Student(name={self.name}, age={self.age})>'