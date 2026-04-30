from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from recipe_model import Recipe
from ..schemas import ingredient_schema

class Ingredient() :
    __tablename__ = "ingredients"
    
    id: Mapped[int] = mapped_column()
    name: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column()
    quantity_kg: Mapped[float] = mapped_column()
    recipes: Mapped[Optional[List["Recipe"]]] = relationship("Recipe", back_populates="ingredients")
    
