from pydantic import BaseModel, Field


class SavingThrows(BaseModel):
    strength: int = Field(..., ge=0, le=3)
    dexterity: int = Field(..., ge=0, le=3)
    constitution: int = Field(..., ge=0, le=3)
    intelligence: int = Field(..., ge=0, le=3)
    wisdom: int = Field(..., ge=0, le=3)
    charisma: int = Field(..., ge=0, le=3)

    class Config:
        validate_assignment = True
