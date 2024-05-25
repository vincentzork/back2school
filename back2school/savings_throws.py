from pydantic import BaseModel, Field


class SavingThrows(BaseModel):
    STR: int = Field(...)
    DEX: int = Field(...)
    CON: int = Field(...)
    INT: int = Field(...)
    WIS: int = Field(...)
    CHA: int = Field(...)

    class Config:
        validate_assignment = True
