from fastapi import FastAPI
import repository
import repository.ingredient_repo
import database as db

app = FastAPI(title="PantryFlow", version="1.0")

app.include_router(repository.ingredient_repo.router)
db.Base.metadata.create_all(bind=db.engine)

@app.post("/test")
def init_test() :
    return {"Status": "Ok"}

