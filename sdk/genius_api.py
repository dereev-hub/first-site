from typing import List
import requests, os
from dotenv import load_dotenv
from pydantic import BaseModel


load_dotenv(override=True)
GENIUS_BEARER_TOKEN = os.getenv("GENIUS_BEARER_TOKEN")


class GeniusHitResult(BaseModel):
    id: int
    title: str


class GeniusHit(BaseModel):
    # higlights: list
    index: str
    type: str
    result: GeniusHitResult


class GeniusResponse(BaseModel):
    hits: List[GeniusHit]


class GeniusResponse(BaseModel):
    meta: BaseModel
    response: GeniusResponse


def search_by_text(text: str) -> GeniusResponse:
    r = requests.get(
        f"https://api.genius.com/search?q={text}",
        headers={
            "Authorization": f"Bearer {GENIUS_BEARER_TOKEN}"
        }
    )
    result = GeniusResponse.model_validate(r.json())
    return result

print([
    song.result for song in
    search_by_text("5 минут назад").response.hits
    ])