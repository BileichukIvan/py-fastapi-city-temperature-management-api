from typing import Optional

from pydantic import BaseModel


class CitySchema(BaseModel):
    name: str
    additional_info: str | None


class CityListSchema(CitySchema):
    id: int

    class Config:
        orm_mode = True


class CityCreateSchema(CitySchema):
    pass


class CityUpdateSchema(CitySchema):
    pass
