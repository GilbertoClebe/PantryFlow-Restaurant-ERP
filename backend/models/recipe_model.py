from sqlalchemy import String, Text, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from ingredient_model import Ingredient
from ..database import Base

recipe_ingredient_assosiation = Table(
    "recipe_ingredient",
    Base.metadata, 
    Column("recipe_id", ForeignKey("recipes.id"), primary_key=True),
    Column("ingrediente_id", ForeignKey("ingredients.id"), primary_key=True)
)

class Recipe() :
    __tablename__ = "recipes"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120))
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[float] = mapped_column()
    ingredients_ids: Mapped[Optional[List["Ingredient"]]] = relationship("Ingredient", back_populates="recipes_ids")
    
    