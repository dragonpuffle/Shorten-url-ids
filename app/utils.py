import hashlib

from fastapi import HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.database import SessionDep
from app.models import UrlsModel
from app.schemas import ShortUrlsSchema


def generate_hash_id(url: str, length: int = 5) -> str:
    hash_object = hashlib.sha256(url.encode())
    hash_hex = hash_object.hexdigest()
    return hash_hex[:length]


async def urls_by_full_url(url: str, session: SessionDep) -> UrlsModel | None:
    query = select(UrlsModel).where(UrlsModel.full_urls == url)
    result = await session.execute(query)
    return result.scalars().first()


async def urls_by_short_url(url: str, session: SessionDep) -> UrlsModel | None:
    query = select(UrlsModel).where(UrlsModel.short_urls == url)
    result = await session.execute(query)
    return result.scalars().first()


async def add_new_url(full_url: str, short_url: str, session: SessionDep) -> ShortUrlsSchema:
    new_url = UrlsModel(full_urls=full_url, short_urls=short_url)
    session.add(new_url)
    try:
        await session.commit()
        return ShortUrlsSchema(short_url=short_url)
    except IntegrityError:
        await session.rollback()
        raise


async def shorten_url(full_url: str, session: SessionDep) -> ShortUrlsSchema:
    existing_url = await urls_by_full_url(full_url, session)
    if existing_url:
        return ShortUrlsSchema(short_url=existing_url.short_urls)

    length = 5
    short_url_id = generate_hash_id(full_url, length)
    while True:
        conflict = await urls_by_short_url(short_url_id, session)
        if not conflict:
            break
        length += 1
        short_url_id = generate_hash_id(full_url, length)

    return await add_new_url(full_url, short_url_id, session)


async def unshorten_url(short_url_id: str, session: SessionDep):
    new_url = await urls_by_short_url(short_url_id, session)
    if not new_url:
        raise HTTPException(status_code=404, detail="Url not found")

    return RedirectResponse(new_url.full_urls, status_code=307)
