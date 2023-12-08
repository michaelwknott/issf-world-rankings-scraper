import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, String, Integer, Date
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column


load_dotenv()

engine = create_engine(os.environ["DB_URL"])
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    """Base class for all models."""

    pass


class Rankings(Base):
    """Model for ISSF world rankings."""

    __tablename__ = "rankings"

    id: Mapped[int] = mapped_column(primary_key=True)
    event: Mapped[str] = mapped_column(String(5))
    rank = mapped_column(Integer)
    rating = mapped_column(Integer)
    name = mapped_column(String(50))
    nation = mapped_column(String)
    year_of_birth = mapped_column(Integer)
    date = mapped_column(Date)
    version_date = mapped_column(Date)
