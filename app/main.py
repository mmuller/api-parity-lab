# main
 
from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from .db import SessionLocal, engine, Base
from .service import create_order
from contextvars import ContextVar
from .context import correlation_id
import uuid
from fastapi import FastAPI, Depends, Request, Header

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/orders")
def create_order_endpoint(
    payload: dict,
    db: Session = Depends(get_db),
    x_bug_mode: str = Header(default=None)
):
    order = create_order(
        db,
        customer=payload.get("customer"),
        amount=payload.get("amount"),
        bug_mode=x_bug_mode   # bug mode
    )

    return {
        "success": True,
        "order_id": order.id,
        "amount": payload.get("amount")  # source of truth API
    }

@app.middleware("http")
async def add_correlation_id(request: Request, call_next):

    bug_mode = request.headers.get("x-bug-mode")

    if bug_mode == "bad_correlation":
        corr_id = "fixed-id"  # bug
    else:
        corr_id = str(uuid.uuid4())

    correlation_id.set(corr_id)

    response = await call_next(request)

    response.headers["X-Correlation-ID"] = corr_id
    return response
