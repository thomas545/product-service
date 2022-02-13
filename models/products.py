from typing import Optional
from pydantic import BaseModel, Field


class BaseProduct(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    category_name: str = Field(...)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., gt=0)


class RetrieveProduct(BaseProduct):
    _id: str = Field(...)


class CreateProduct(BaseProduct):
    pass


class UpdateProduct(BaseModel):
    title = Optional[str]
    description = Optional[str]
    category_name = Optional[str]
    price = Optional[float]
    quantity = Optional[int]

    class Config:
        arbitrary_types_allowed = True
