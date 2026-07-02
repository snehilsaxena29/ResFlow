from fastapi import APIRouter

from src.core.constants import HEALTH_MESSAGE

router = APIRouter(tags=["Health"])


@router.get("/health")
def health_check():
    return {
        "status": HEALTH_MESSAGE
    }