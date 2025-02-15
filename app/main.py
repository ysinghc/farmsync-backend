from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.auth import router as auth_router
from app.database import SessionLocal
from app import crud, schemas
from app.routes.orders import router as orders_router

app = FastAPI()

# ✅ Allow frontend to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change "*" to ["https://home.farmsync.ysinghc.me"] for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include authentication & registration routes
app.include_router(auth_router, prefix="/auth")
app.include_router(orders_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to FarmSync API"}
