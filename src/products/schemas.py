from pydantic import BaseModel, Field


class ProductsCreateSchema(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    price: int = Field(gt=0)
    description: str | None = Field(default=None, min_length=10)
    category: str = Field(min_length=3, max_length=100)


class ProductsUpdateSchema(BaseModel):
    name: str | None = Field(default=None, min_length=3, max_length=100)
    price: int | None = Field(default=None, gt=0)
    description: str | None = Field(default=None, min_length=10)
    category: str | None = Field(default=None, min_length=3, max_length=100)