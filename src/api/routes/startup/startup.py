from fastapi import APIRouter

from freemocap.prod.cam.detection.cam_singleton import get_or_create_cams

startup_router = APIRouter()


@startup_router.on_event('startup')
async def handle_startup():
    get_or_create_cams()
