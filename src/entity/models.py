from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import EmailStr

from src.database.db import Base


class Contact(Base):
    __tablename__ = "contact"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    lastName: Mapped[str] = mapped_column(String(50))
    email: Mapped[EmailStr] = mapped_column(String(50), unique=True)
    phoneNumber: Mapped[int] = mapped_column(unique=True)
    birthDate: Mapped[Date] = mapped_column(Date)
    rest: Mapped[str] = mapped_column(String(500))
