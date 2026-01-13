from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass  # <- Add this

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True  # In Pydantic v2, you can also use `from_attributes = True`
