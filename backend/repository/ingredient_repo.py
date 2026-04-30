from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import service.ingredient_service as service
import database
import schemas.ingredient_schema as schema
router = APIRouter()

@router.post("/create", response_model=schema.IngredientResponse)
def create_ingredient(ingredient: schema.IngredientCreate, db: Session = Depends(database.get_db)) :

    new_ingredient = service.object_conversion(ingredient)
    if not new_ingredient : 
        raise HTTPException(status_code=422, detail="The conversion has failed")
    db.add(new_ingredient)
    db.commit()
    db.refresh(new_ingredient)
    return new_ingredient


    