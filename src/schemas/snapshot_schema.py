from datetime import datetime

from pydantic import BaseModel


class Doc(BaseModel):
    _id: datetime
    _rev: str
    container: str
    timestamp: datetime
    current_stock: list[str]


class Value(BaseModel):
    rev: str


class Snapshot(BaseModel):
    """class that represent a Photo of the
    inventory with a list of EPCs that correspond to items"""

    id: datetime
    key: datetime
    value: Value
    doc: Doc
