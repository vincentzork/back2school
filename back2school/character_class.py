from pydantic import BaseModel


class CharacterClass(BaseModel):
    class_name: str
    archetype: str
    level: int
