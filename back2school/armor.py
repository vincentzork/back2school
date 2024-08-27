from pydantic import BaseModel


class Armor(BaseModel):
    name: str
    armor_type: str
    armor_class: int
    special_properties: str
