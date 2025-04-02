from sqlalchemy import Column, Integer, String , DateTime, Enum
from datetime import datetime
from database import Base

class LeaveRequest(Base):
    __tablename__ = "leave_requests"
    id = Column(Integer,primary_key = True, index = True)
    employee_id = Column(String, index = True)
    start_date = Column(String)
    end_date = Column(String)
    leave_type = Column(String)
    reason = Column(String)
    status = Column(String, default = "PENDING")
    working_days = Column(Integer)
    created_at = Column(DateTime, default = datetime.utcnow)