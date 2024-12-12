from pydantic import BaseModel, EmailStr


class UserAuthSchema(BaseModel):
    id: int
    

class TokenResponseSchema(BaseModel):
    access_token: str
    token_type: str
