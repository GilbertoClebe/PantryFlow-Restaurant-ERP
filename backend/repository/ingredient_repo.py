from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import service.ingredient_service as service
import models.ingredient_model as model
import schemas.ingredient_schema as schema
import database
router = APIRouter()

@router.post("/", response_model=schema.IngredientResponse)
def create_ingredient(ingredient: schema.IngredientCreate, db: Session = Depends(database.get_db)) :

    new_ingredient = service.object_conversion(ingredient)
    if not new_ingredient : 
        raise HTTPException(status_code=422, detail="The conversion has failed")
    db.add(new_ingredient)
    db.commit()
    db.refresh(new_ingredient)
    return new_ingredient

@router.get("/{id}")
def get_ingredient_id(id: int, db: Session = Depends(database.get_db)) :
    found_ingredient = db.get(model.Ingredient, id)
    if not found_ingredient :
        raise HTTPException(status_code=404, detail="We cannot find the ingredient!")
    return found_ingredient
    