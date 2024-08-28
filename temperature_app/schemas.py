from datetime import datetime

from pydantic import BaseModel

from city_app.schemas import CitySchema


class TemperatureBaseSchema(BaseModel):
    city_id: int
    date_time: datetime
    temperature: float


class TemperatureCitySchema(TemperatureBaseSchema):
    id: int
    city: CitySchema

    class Config:
        from_attributes = True


class TemperatureCreateSchema(TemperatureBaseSchema):
    pass
