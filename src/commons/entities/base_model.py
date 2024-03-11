from sqlalchemy import Column, String, func, DateTime, ForeignKey

from src.commons.config.database import Base


class BaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime, default=func.now())
    created_by = Column(String(length=36), ForeignKey('users.id'))
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    updated_by = Column(String(length=36), ForeignKey('users.id'))

    def save(self, session, user_id):
        if not self.created_by:
            self.created_by = user_id
        self.updated_by = user_id
        session.add(self)
        session.commit()
