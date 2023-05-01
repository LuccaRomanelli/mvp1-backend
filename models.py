from sqlalchemy import Column, Integer, String
from database import Base

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    type = Column(String)
    rating = Column(Integer)
    description = Column(String)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'year': self.year,
            'type': self.type,
            'rating': self.rating,
            'description': self.description
        }
