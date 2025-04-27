from pydantic import BaseModel, HttpUrl


class UrlsSchema(BaseModel):
    url: HttpUrl


class ShortUrlsSchema(BaseModel):
    short_url: str
