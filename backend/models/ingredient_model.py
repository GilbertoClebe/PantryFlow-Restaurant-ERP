
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from typing import Optional, List

from ..database import Base

class Ingredient(Base) :
    __tablename__ = "ingredients"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120))
    price: Mapped[float] = mapped_column()
    quantity_kg: Mapped[float] = mapped_column()
    recipes: Mapped[Optional[List["Recipe"]]] = relationship("Recipe", back_populates="ingredients")
    
