from pydantic import BaseModel, ConfigDict


class CitySchema(BaseModel):
    name: str
    additional_info: str | None


class CityListSchema(CitySchema):
    id: int

    model_config = ConfigDict(from_orm=True)


class CityCreateSchema(CitySchema):
    pass


class CityUpdateSchema(CitySchema):
    pass
