from fastapi import APIRouter

from app.database import SessionDep
from app.schemas import UrlsSchema, ShortUrlsSchema
from app.utils import shorten_url, unshorten_url

router = APIRouter()


@router.post('/', status_code=201, response_model=ShortUrlsSchema)
async def shorten_url_route(full_url: UrlsSchema, session: SessionDep):
    result = await shorten_url(full_url, session)
    return result


@router.get('/{shorten_url_id}', status_code=307)
async def get_original_url_route(shorten_url_id: str, session: SessionDep):
    result = await unshorten_url(shorten_url_id, session)
    return result
