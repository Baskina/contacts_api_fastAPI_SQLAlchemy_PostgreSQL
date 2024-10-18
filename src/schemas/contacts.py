from pydantic import BaseModel, EmailStr, Field, PastDatetime


# validation Schemas

class ContactValidationSchema(BaseModel):
    name: str
    lastName: str
    email: EmailStr
    phoneNumber: int
    birthDate: PastDatetime
    rest: str


class ContactValidationSchemaResponse(ContactValidationSchema):
    id: int = 1

    class Config:
        from_attributes = True
