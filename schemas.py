from pydantic import BaseModel, Field
class GenerateRequest(BaseModel):
    prompt: str = Field(min_length=3, max_length=2000)
    size: str = "1024x1024"
    quality: str = "medium"
    style: str = "natural"
