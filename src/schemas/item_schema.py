from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, validator


class Batch(BaseModel):
    id: str
    exp: datetime

    @validator("exp", pre=True, allow_reuse=True)
    def parse_date_field(cls, value):
        if isinstance(value, datetime):
            return value
        try:
            # Attempt to parse the date string into a datetime object
            return datetime.strptime(value, "%Y-%m-%d")
        except (ValueError, TypeError):
            try:
                # Attempt to parse the datetime string into a datetime object
                return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
            except (ValueError, TypeError):
                raise ValueError(
                    'Invalid date format. Use "YYYY-MM-DD" or "YYYY-MM-DDTHH:MM:SS.sssZ".'
                )


class Product(BaseModel):
    _id: str
    cfn: str
    description: str


class User(BaseModel):
    _id: str
    rut: str
    name: str
    second_name: str
    last_name: str
    supervisor: bool
    position: str
    description: str
    created_at: str
    updated_at: str
    containers: List[str]
    allow_all: bool
    login_at: str
    last_login_as: str
    closed_at: str
    logout_at: str


class HistoryEvent(BaseModel):
    event: str
    date: datetime
    user: Optional[User | dict]
    device_id: str
    patient_id: str
    location: str
    session: Optional[str]


class Doc(BaseModel):
    _id: str
    _rev: str
    epc: str
    gtin: str
    gs1: str
    batch: Batch
    container_id: str
    created_at: datetime
    product_cfn: str
    dispatch: Optional[str]
    product: Product
    history: list[HistoryEvent]


class Value(BaseModel):
    rev: str


class Item(BaseModel):
    id: str
    key: str
    value: Value
    doc: Doc
