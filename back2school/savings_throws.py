from pydantic import BaseModel, Field


class SavingThrows(BaseModel):
    strength: int = Field(...)
    dexterity: int = Field(...)
    constitution: int = Field(...)
    intelligence: int = Field(...)
    wisdom: int = Field(...)
    charisma: int = Field(...)

    class Config:
        validate_assignment = True
