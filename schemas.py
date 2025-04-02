from pydantic import BaseModel, Field
from datetime import datetime

class LeaveRequestCreate(BaseModel):
    employee_id: str
    start_date : str
    end_date :str
    leave_type: str = Field(pattern = "^(ANNUAL|SICK|PERSONAL)$")
    reason: str = Field(min_length= 10)


class LeaveRequestResponse(BaseModel):

    id:int
    employee_id : str
    start_date : str
    end_date :str
    leave_type: str
    reason: str
    status: str
    working_days :int
    created_at : datetime
