from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import RedirectResponse

from city_app import crud, schemas
from dependencies import get_db

router = APIRouter()


@router.get("/cities/", response_model=list[schemas.CityListSchema])
async def get_cities_list(
        skip: int = 0,
        limit: int = 10,
        db: AsyncSession = Depends(get_db)
) -> list[schemas.CityListSchema]:
    return await crud.get_cities_list(db=db, skip=skip, limit=limit)


@router.post("/cities/", response_model=schemas.CitySchema)
async def create_city(
        city: schemas.CityCreateSchema, db: AsyncSession = Depends(get_db)
) -> schemas.CitySchema:
    return await crud.create_city(db=db, city=city)


@router.get("/cities/{city_id}", response_model=schemas.CitySchema)
async def get_city(
        city_id: int, db: AsyncSession = Depends(get_db)
) -> schemas.CitySchema:
    return await crud.get_city(city_id=city_id, db=db)


@router.put("/cities/{city_id}", response_model=schemas.CitySchema)
async def update_city(
        city_id: int,
        city: schemas.CityUpdateSchema,
        db: AsyncSession = Depends(get_db)
):
    db_city = await crud.get_city(db, city_id=city_id)
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return await crud.update_city(db=db, city=city, city_id=city_id)


@router.delete("/cities/{city_id}", response_model=schemas.CityUpdateSchema)
async def delete_city(
        city_id: int, db: AsyncSession = Depends(get_db)
) -> RedirectResponse:
    db_city = await crud.delete_city_from_db(db=db, city_id=city_id)
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return await db_city
