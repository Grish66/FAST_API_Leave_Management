from sqlalchemy.orm import Session
from models import LeaveRequest
from datetime import datetime, timedelta
from schemas import LeaveRequestCreate


def overloapping(db: Session, emp_id :str, start:str, end:str):
    return db.query(LeaveRequest).filter(LeaveRequest.employee_id ==emp_id,
                                         LeaveRequest.start_date <= end, 
                                         LeaveRequest.end_date >= start).first()

def calculate_working_days(start_date: str, end_date :str):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    day_count = 0

    for i in range((end-start).days+1):
        if( start + timedelta(days=i)).weekday() < 5:
            day_count += 1
    return day_count



def create_leave_request(db: Session, data: LeaveRequestCreate):
    start = datetime.strptime(data.start_date, "%Y-%m-%d")
    end = datetime.strptime(data.end_date, "%Y-%m-%d")

    if end <= start:
        raise  ValueError("End Date must be after the start date")
    working_days= calculate_working_days(data.start_date,data.end_date)
    if working_days > 14:
        raise ValueError("Overall Leaves are 14")
    if overloapping(db, data.employee_id, data.start_date, data.end_date):
        raise ValueError("Overlapping the leave")    
    
    leave = LeaveRequest(
        employee_id = data.employee_id,
        start_date = data.start_date,
        end_date = data.end_date,
        leave_type = data.leave_type,
        reason = data.reason,
        working_days = working_days
    )

    db.add(leave)
    db.commit()
    db.refresh(leave)
    return leave


