from pydantic import BaseModel


class ImageList(BaseModel):
    results: list[str] = []
