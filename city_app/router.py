from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from city_app import crud, schemas
from dependencies import get_db

router = APIRouter()


@router.get("/cities/", response_model=list[schemas.CityListSchema])
def get_cities_list(
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)
) -> list[schemas.CityListSchema]:
    return crud.get_cities_list(db=db, skip=skip, limit=limit)


@router.post("/cities/", response_model=schemas.CitySchema)
def create_city(
        city: schemas.CityCreateSchema, db: Session = Depends(get_db)
) -> schemas.CitySchema:
    return crud.create_city(db=db, city=city)


@router.get("/cities/{city_id}", response_model=schemas.CitySchema)
def get_city(
        city_id: int, db: Session = Depends(get_db)
) -> schemas.CitySchema:
    return crud.get_city(city_id=city_id, db=db)


@router.delete("/cities/{city_id}", response_model=schemas.CitySchema)
def delete_city(
        city_id: int, db: Session = Depends(get_db)
) -> RedirectResponse:
    db_city = crud.delete_city_from_db(db=db, city_id=city_id)
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return db_city
