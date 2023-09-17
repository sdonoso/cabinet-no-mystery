from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Batch(BaseModel):
    id: str
    exp: datetime


class Product(BaseModel):
    _id: str
    cfn: str
    description: str


class HistoryEvent(BaseModel):
    event: str
    date: datetime
    user: dict
    device_id: str
    patient_id: str
    location: str


class DocRemoved(BaseModel):
    _id: str
    _rev: str
    epc: str
    gtin: str
    gs1: str
    batch: Batch
    container_id: str
    created_at: datetime
    product_cfn: str
    product: Product
    history: list[HistoryEvent]
    consumed: bool


class Doc(BaseModel):
    _id: str
    _rev: str
    added: list[Optional[dict]]
    removed: list[DocRemoved]
    container_id: str
    created_at: datetime
    session_uuid: str
    patient_id: str
    user: dict
    type: str


class Value(BaseModel):
    rev: str


class Session(BaseModel):
    """User sessions that interacted with the system"""

    id: str
    key: str
    value: Value
    doc: Doc
