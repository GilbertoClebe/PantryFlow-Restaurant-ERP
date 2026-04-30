from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
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
    if db.execute(select(model.Ingredient).where(model.Ingredient.name == new_ingredient.name)) :
        raise HTTPException(status_code=409, detail="This ingredient alredy exists...")
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

@router.get("/{name}")
def get_ingredient_name(name: str, db: Session = Depends(database.get_db)) :
    found_ingredient = db.execute(select(model.Ingredient).where(model.Ingredient.name == name))
    if not found_ingredient :
        raise HTTPException(status_code=404, detail="We cannot find the ingredient")
    if db.execute(select(model.Ingredient).where(model.Ingredient.name == found_ingredient.name)) :
        raise HTTPException(status_code=409, detail="Have two or more identical objects in system...")
    return found_ingredient