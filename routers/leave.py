from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import LeaveRequestCreate, LeaveRequestResponse
from service import create_leave_request
from models import  LeaveRequest


router = APIRouter()



def get_db():
    db= SessionLocal()
    try:
        yield db

    finally:
        db.close()

@router.post("/leave-requests", response_model=LeaveRequestResponse)
def create_leave(data: LeaveRequestCreate, db: Session = Depends(get_db)):
    try: 
        return create_leave_request(db, data)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    

@router.get("/leave-requests/{employee_id}", response_model= list[LeaveRequestResponse])
def get_leaves(employee_id: str, db:Session = Depends(get_db)):
    return db.query(LeaveRequest).filter(LeaveRequest.employee_id == employee_id).all()