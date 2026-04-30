import schemas.ingredient_schema as schema
import models.ingredient_model as model
def object_conversion(ingredient: schema.IngredientResponse) :
    return model.Ingredient(
        id = ingredient.id,
        name = ingredient.name,
        price = ingredient.price,
        quantity_kg = ingredient.quantity_kg,
        recipes = None #Ajeitar o loop depois
    )
