from pydantic import BaseModel, Field, field_validator
import re

class Structure(BaseModel):
    tldr: str = Field(description="generate a too long; didn't read summary")
    motivation: str = Field(description="describe the motivation in this paper")
    method: str = Field(description="rewrite the method in plain and clear academic language, avoiding vague or abstract terms")
    result: str = Field(description="result of this paper")
    conclusion: str = Field(description="conclusion of this paper")
