from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List
from recipe_schema import RecipeResponse

class IngredientBase(BaseModel) :
    name: str
    price: float = Field(gt=0)
    quantity_kg: float = Field(gt=0)
    
class IngredientCreate(IngredientBase()) :
    recipes: Optional[List["RecipeResponse"]]   
    model_config = ConfigDict({"from_attributes": True})
    
class IngredientResponse(IngredientBase()) :
    id: int
    recipes: Optional[List["RecipeResponse"]]   
    model_config = ConfigDict({"from_attributes": True})
    
class IngredientUpdate(BaseModel) :
    name: Optional[str] 
    price: Optional[float] = Field(gt=0)
    quantity_kg: Optional[float] = Field(gt=0)
    recipes: Optional[List["RecipeResponse"]]  
    
IngredientResponse.model_rebuild()