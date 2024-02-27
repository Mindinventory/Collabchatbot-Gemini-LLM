import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from api import routers
from fastapi.middleware.cors import CORSMiddleware
from db.cache.caching import cache_all
from apitally.fastapi import ApitallyMiddleware

cache_all()

app = FastAPI(
    description="API fpr the Collab Chatbot to generate intent based query response",
    title="Collab Chatbot",
    version="0.0.1",
)

# Add route for APIs
app.include_router(routers.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    ApitallyMiddleware,
    client_id="501bd99c-82a7-4e4e-8c93-60410ff080ae",
    env="dev",  # or "dev"
)


@app.get("/")
async def index():
    return "User Auth Service is running."


@app.exception_handler(Exception)
async def unicorn_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400, content={"message": "Oops! Something went wrong..."}
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
