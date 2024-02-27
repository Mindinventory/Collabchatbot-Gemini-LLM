from fastapi import APIRouter

from .v1.views import question

# Add route with prefix /api/v1 to manage v1 APIs.
router = APIRouter(prefix="/api/v1/question-service")
router.include_router(question.router, tags=["Question Service Endpoints"])
