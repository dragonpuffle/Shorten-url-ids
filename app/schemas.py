from pydantic import BaseModel, HttpUrl


class UrlsSchema(BaseModel):
    url: HttpUrl


class UrlsDBSchema(BaseModel):
    full_urls: HttpUrl
    short_urls: str


class ShortUrlsSchema(BaseModel):
    short_url: str
