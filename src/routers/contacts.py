from fastapi import APIRouter, Depends, status, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.contacts import ContactValidationSchemaResponse, ContactValidationSchema
from src.database.db import get_db

from src.repository import contacts as repositories_contacts

routerContacts = APIRouter(prefix='/contacts', tags=['contacts'])


@routerContacts.get("/", response_model=list[ContactValidationSchemaResponse])
async def read_all_contacts(limit: int = Query(default=10, ge=10, le=10), offset: int = Query(default=0, ge=0),
                            name: str = Query(default=None),
                            lastName: str = Query(default=None),
                            email: str = Query(default=None),
                            findBD: bool = Query(default=False),
                            db: AsyncSession = Depends(get_db)):
    contacts = await repositories_contacts.read_all_contacts(limit, offset, name, lastName, email, findBD, db)
    return contacts


@routerContacts.get("/{contact_id}", response_model=ContactValidationSchemaResponse)
async def read_contact(contact_id: int = Path(ge=1), db: AsyncSession = Depends(get_db)):
    contact = await repositories_contacts.read_contact(contact_id, db)

    return contact


@routerContacts.post("/", response_model=ContactValidationSchemaResponse, status_code=status.HTTP_201_CREATED)
async def add_contact(body: ContactValidationSchema, db: AsyncSession = Depends(get_db)):
    contact = await repositories_contacts.add_contact(body, db)

    return contact


@routerContacts.put("/{contact_id}")
async def update_contact(body: ContactValidationSchemaResponse, contact_id: int,
                         db: AsyncSession = Depends(get_db)):
    contact = await repositories_contacts.update_contact(body, contact_id, db)

    return contact


@routerContacts.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(contact_id: int = Path(ge=1), db: AsyncSession = Depends(get_db)):
    await repositories_contacts.delete_contact(contact_id, db)
