from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List


class IngredientBase(BaseModel) :
    name: str
    price: float = Field(gt=0)
    quantity_kg: float = Field(gt=0)
    
class IngredientCreate(IngredientBase) :
    recipes_ids: Optional[List[int]]   
    model_config = ConfigDict({"from_attributes": True})
    
class IngredientResponse(IngredientBase) :
    id: int
    recipes_ids: Optional[List[int]]   
    model_config = ConfigDict({"from_attributes": True})
    
class IngredientUpdate(BaseModel) :
    name: Optional[str] 
    price: Optional[float] = Field(gt=0)
    quantity_kg: Optional[float] = Field(gt=0)
    recipes_ids: Optional[List[int]]  

class IngredientSample(BaseModel) :
    id: int
    name: str
    price: float = Field(gt=0)
    model_config = ConfigDict({"from_attributes": True})
    
IngredientResponse.model_rebuild()