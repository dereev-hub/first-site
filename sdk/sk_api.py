import base64
import os

from dotenv import load_dotenv
from pydantic import BaseModel
import requests

class SKResultTrack(BaseModel):
    kind: str 
    id: int
    urn: str
    created_at: str
    duration: int
    commentable: bool | None = None
    comment_count: int | None = None
    sharing: str | None = None
    tag_list: str | None = None
    streamable: bool | None = None
    embeddable_by: str | None = None
    purchase_url: str | None = None
    purchase_title: str | None = None
    genre: str | None = None
    title: str
    description: str | None = None
    label_name: str | None = None
    release: bool | None = None
    key_signature: bool | None = None
    isrc: str | None = None
    bpm: bool | None = None
    release_year: int | None = None
    release_month: int | None = None
    release_day: int | None = None
    license: str | None = None
    uri: str | None = None



class SKApi:

    def __init__(self, client_id:str , client_secret:str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_token = None
    
    def _get_base64_token(self)-> str:
        encoded = base64.b64encode(f"{self.client_id}:{self.client_secret}".encode("utf-8"))
        return encoded.decode("utf-8")
    
    def auth(self)-> dict:
        r = requests.post(
            "https://secure.soundcloud.com/oauth/token",
            headers={
                "accept": "application/json; charset=utf-8",
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": f"Basic {self._get_base64_token()}"
            },
            data = {
                "grant_type": "client_credentials"
            }
        )
        if r.status_code < 300:
            return r.json()


    def search_by_title(self, title:str):
        if self.auth_token is None:
            self.auth_token = self.auth().get("access_token")
        r = requests.get(
            f"https://api.soundcloud.com/tracks?q={title}",
            headers={
                "Authorization": f"Bearer {self.auth_token}",
                "accept": "application/json; charset=utf-8"
            }
        )
        return [SKResultTrack.model_validate(track) for track in r.json()]
        
if __name__ == "__main__":
    load_dotenv()
    skapi=SKApi(os.getenv("SK_CLIENT_ID"), os.getenv("SK_CLIENT_SECRET"))
    print(skapi.search_by_title("5 минут назад"))