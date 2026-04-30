from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List

class RecipeBase(BaseModel) :
    name: str
    description: str
    price: float = Field(gt=0)
    model_config = ConfigDict({"from_attributes": True})
    
class RecipeCreate(RecipeBase) :
    ingredients_ids: Optional[List[int]]

class RecipeResponse(RecipeBase) :
    id: int
    ingredients_ids: Optional[List[int]]

class RecipeUpdate(BaseModel) :
    name: Optional[str]
    description: Optional[str]
    price: Optional[float] = Field(gt=0)
    model_config = ConfigDict({"from_attributes": True})
    
RecipeResponse.model_rebuild()
    