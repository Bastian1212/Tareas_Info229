


from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base #Se importa el objeto Base desde el archivo database.py

class new(Base): 

    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), unique=True, index=True)
    date =  Column(String(50))
    url =  Column(String(100))
    media_outlet =  Column(String(100))

    items = relationship("has_category", back_populates="owner")

class has_category(Base):

    __tablename__ = "category"

    id = Column(Integer, primary_key=True,index=True)
    value = Column(String(50), index=True)
    id2 = Column(Integer,ForeignKey("news.id"))

    owner = relationship("news", back_populates="category")
