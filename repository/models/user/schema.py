from pydantic import BaseModel, EmailStr, Field


# properties required during user creation
class UserCreate(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=4)
    password: str = Field(..., min_length=4)
    fullname: str = Field(..., min_length=4)
    avatar: str = ''
    