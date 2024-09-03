from datetime import datetime

from pydantic import BaseModel

from city_app.schemas import CitySchema


class TemperatureBaseSchema(BaseModel):
    city_id: int
    date_time: datetime | None
    temperature: float | None


class TemperatureCitySchema(TemperatureBaseSchema):
    id: int
    city: CitySchema

    class Config:
        orm_mode = True


class TemperatureCreateSchema(TemperatureBaseSchema):
    pass
