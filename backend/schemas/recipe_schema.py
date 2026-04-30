from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List
from ingredient_schema import IngredientResponse, IngredientSample

class RecipeBase(BaseModel) :
    name: str
    description: str
    price: float = Field(gt=0)
    model_config = ConfigDict({"from_attributes": True})
    
class RecipeCreate(RecipeBase) :
    ingredients: Optional[List["IngredientSample"]]

class RecipeResponse(RecipeBase) :
    id: int
    ingredients: Optional[List["IngredientSample"]]

class RecipeUpdate(BaseModel) :
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    model_config = ConfigDict({"from_attributes": True})
    

    