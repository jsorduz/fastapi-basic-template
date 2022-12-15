from fastapi import FastAPI
from fastapi.logger import logger

from app.api.v1.api import router as router_v1
from app.config.settings import get_settings


async def on_startup() -> None:
    logger.info("on_startup")


async def on_shutdown() -> None:
    logger.info("on_shutdown")


def get_application() -> FastAPI:
    settings = get_settings()
    application = FastAPI(
        title=settings.title,
        version=settings.version,
        debug=settings.debug,
        openapi_url=f"{settings.api_prefix_v1}{settings.api_openapi}",
        docs_url=f"{settings.api_prefix_v1}{settings.api_docs}",
        on_startup=(on_startup,),
        on_shutdown=(on_shutdown,),
    )

    application.include_router(router_v1, prefix=settings.api_prefix_v1)

    return application


app = get_application()
