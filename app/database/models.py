from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.database.database import Base


class Experiment(Base):

    __tablename__ = "experiments"

    id = Column(Integer, primary_key=True, index=True)

    experiment_id = Column(String)

    strategy = Column(String)

    original_prompt = Column(Text)

    attacked_prompt = Column(Text)

    response = Column(Text)

    safe = Column(Boolean)

    risk_score = Column(Float)

    created_at = Column(DateTime)