from fastapi.testclient import TestClient

from main import app

client = TestClient(app)
def test_create_leave():

    payload = {

        "employee_id": "EMP001",
        "start_date": "2025-04-01",
        "end_date": "2025-04-05",
        "leave_type": "ANNUAL",
        "reason": "Family Vacation"

    }
    response = client.post("/api/v1/leave-requests", json = payload)
    assert response.status_code == 200
    assert response.json()['status'] == 'PENDING'



def test_create_leave_invalid():
    payload = {
            
            
        "employee_id": "EMP05",
        "start_date": "2025-04-05",
        "end_date": "2025-04-01",
        "leave_type": "ANNUAL",
        "reason": "iNVALID Date"

    }
    response = client.post("/api/v1/leave-requests", json=payload)
    assert response.status_code == 400


