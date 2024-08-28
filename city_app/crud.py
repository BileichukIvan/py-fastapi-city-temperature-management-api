from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from city_app import models, schemas


def create_city(db: Session, city: schemas.CityCreateSchema) -> models.City:
    db_city = models.City(
        name=city.name,
        additional_info=city.additional_info
    )
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city


def get_city(db: Session, city_id: int) -> models.City:
    city = db.query(models.City).filter(models.City.id == city_id).first()
    return city


def get_cities_list(
        db: Session | AsyncSession, skip: int = 0, limit: int = 10
) -> list[models.City]:
    return db.query(models.City).offset(skip).limit(limit).all()


def delete_city(db: Session, city_id: int) -> None:
    db.query(models.City).filter(models.City.id == city_id).delete()
    db.commit()
