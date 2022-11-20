import logging
from typing import Callable

from fastapi import Request, Response
from fastapi.routing import APIRoute


# This can be used for logging but is obnoxious
# user_router = APIRouter(route_class=LoggerRoute)


class LoggerRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            req = await request.body()
            logging.info(
                f"Request at {request.url} \nrequest body: {req!r} \nrequest headers: {request.headers}"
            )
            response: Response = await original_route_handler(request)
            logging.info(f"Request at {request.url}\nresponse body : {response.body!r}")
            return response

        return custom_route_handler
