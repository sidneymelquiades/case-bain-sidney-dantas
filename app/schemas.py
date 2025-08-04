from pydantic import BaseModel, validator, ValidationError
from typing import Literal

from pydantic import BaseModel, Field, field_validator
from typing import Literal

class PropertyInput(BaseModel):
    type: Literal["departamento", "casa"]
    sector: Literal['vitacura','la reina','las condes','lo barnechea','providencia','nunoa']
    net_usable_area: float
    net_area: float
    n_rooms: int
    n_bathroom: int
    latitude: float
    longitude: float

    # Áreas e números devem ser maiores que zero
    @field_validator('net_usable_area', 'net_area')
    @classmethod
    def must_be_positive(cls, v, info):
        if v <= 0:
            raise ValueError(f"{info.title or info.name} deve ser maior que zero")
        return v

    # Latitude entre -34 e -30
    @field_validator('latitude')
    @classmethod
    def latitude_range(cls, v):
        if not (-34 <= v <= -30):
            raise ValueError('latitude deve estar entre -34 e -30')
        return v

    # Longitude entre -73 e -68
    @field_validator('longitude')
    @classmethod
    def longitude_range(cls, v):
        if not (-73 <= v <= -68):
            raise ValueError('longitude deve estar entre -73 e -68')
        return v

class PredictionOutput(BaseModel):
    price: float

