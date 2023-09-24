from . import data 
from sqlalchemy.orm import Mapped, mapped_column

class Sample(data.Model):
    id: Mapped[int] = mapped_column(data.Integer, primary_key=True)
    initials: Mapped[str] = mapped_column(data.String, nullable=False)
    age: Mapped[int] = mapped_column(data.Integer)

class Megalovania(data.Model):
    id: Mapped[int] = mapped_column(data.Integer, primary_key=True, unique=True)
    link: Mapped[str] = mapped_column(data.String, nullable=False, unique=True)
    type: Mapped[str] = mapped_column(data.String, nullable=False, unique=True)
    elo: Mapped[float] = mapped_column(data.Float, nullable=False)

class WetHands(data.Model):
    id: Mapped[int] = mapped_column(data.Integer, primary_key=True, unique=True)
    link: Mapped[str] = mapped_column(data.String, nullable=False, unique=True)
    type: Mapped[str] = mapped_column(data.String, nullable=False, unique=True)
    elo: Mapped[float] = mapped_column(data.Float, nullable=False)

class Pigstep(data.Model):
    id: Mapped[int] = mapped_column(data.Integer, primary_key=True, unique=True)
    link: Mapped[str] = mapped_column(data.String, nullable=False, unique=True)
    type: Mapped[str] = mapped_column(data.String, nullable=False, unique=True)
    elo: Mapped[float] = mapped_column(data.Float, nullable=False)

class Otherside(data.Model):
    id: Mapped[int] = mapped_column(data.Integer, primary_key=True, unique=True)
    link: Mapped[str] = mapped_column(data.String, nullable=False, unique=True)
    type: Mapped[str] = mapped_column(data.String, nullable=False, unique=True)
    elo: Mapped[float] = mapped_column(data.Float, nullable=False)

class FurElise(data.Model):
    id: Mapped[int] = mapped_column(data.Integer, primary_key=True, unique=True)
    link: Mapped[str] = mapped_column(data.String, nullable=False, unique=True)
    type: Mapped[str] = mapped_column(data.String, nullable=False, unique=True)
    elo: Mapped[float] = mapped_column(data.Float, nullable=False)