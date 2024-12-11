from pydantic import BaseModel, EmailStr


class UserAuthSchema(BaseModel):
    email: EmailStr
    password: str
    

class TokenResponseSchema(BaseModel):
    access_token: str
    token_type: str
