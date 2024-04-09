import typing

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import JSONResponse, RedirectResponse
import orjson
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware

from app.views.api_router import api_router


class ORJSONResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return orjson.dumps(content)


origins = [
    "http://localhost:3000",
    "localhost:3000",
    "*"
]
app = FastAPI(default_response_class=ORJSONResponse)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)


@app.get('/')
@app.post('/')
def root():
    return RedirectResponse(url='/docs')
