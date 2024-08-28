from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from temperature_app import models
from temperature_app.schemas import TemperatureCreateSchema


def create_temperature(
        db: Session | AsyncSession,
        temperature: TemperatureCreateSchema
) -> models.Temperature:
    db_temperature = models.Temperature(**temperature.dict())
    db.add(db_temperature)
    db.commit()
    db.refresh(db_temperature)
    return db_temperature


def get_temperatures(
        db: Session, skip: int = 0, limit: int = 10
) -> list[models.Temperature]:
    return db.query(models.Temperature).offset(skip).limit(limit).all()


def get_temperatures_by_city_id(db: Session, city_id: int):
    return db.query(models.Temperature).filter(
        models.Temperature.city_id == city_id
    ).all()
