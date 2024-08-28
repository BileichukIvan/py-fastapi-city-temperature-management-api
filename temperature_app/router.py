import os
from city_app import crud as city_crud
from dependencies import get_db
from temperature_app import crud, schemas
import httpx
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()
weather_api_key = os.getenv("WEATHER_API_KEY")


@router.post("/temperatures/update")
async def get_temperatures_list(db: AsyncSession = Depends(get_db)):
    cities = city_crud.get_cities_list(db)
    weather_url = "http://api.weatherapi.com/v1/current.json"
    async with httpx.AsyncClient() as client:
        for city in cities:
            params = {"key": weather_api_key, "q": city}
            response = await client.get(weather_url, params=params)
            data = response.json()
            temperature_data = schemas.TemperatureCreateSchema(
                city_id=city.id,
                date_time=data["current"]["last_updated"],
                temperature=data["current"]["temp_c"]
            )
            crud.create_temperature(db=db, temperature=temperature_data)

        return {"message": "Temp updated"}


@router.get(
    "/temperatures", response_model=list[schemas.TemperatureCitySchema]
)
def get_temperatures(
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)
) -> list[schemas.TemperatureCitySchema]:
    return crud.get_temperatures(db=db, skip=skip, limit=limit)


@router.get("/temperatures/{city_id}")
def update_temperatures(
        city_id: int, db: Session = Depends(get_db)
) -> schemas.TemperatureCitySchema:
    return crud.get_temperatures_by_city_id(db=db, city_id=city_id)
