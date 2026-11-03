from fastapi import FastAPI
from pydantic import BaseModel, Field 

app = FastAPI(
    title="Security Data Engineering Lab",
    description="A learning backend for security and data engineering.",
    version="0.1.0"
)

class Transaction(BaseModel):
    amount: float = Field(gt=0)

@app.get("/")
def home():
    return {
        "message": "Welcome to Security Data Engineering Lab",
        "status": "running"
    }

@app.post("/transactions")
def create_transaction(transaction: Transaction):
    return {
        "message": "Transaction data received successfully",
        "amount": transaction.amount,
        "currency": "KES",
        "status": "accepted"
    }
