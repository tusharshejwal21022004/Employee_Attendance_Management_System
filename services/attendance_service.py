attendance_records = []

def mark_attendance(employee_id, attendance_date):
    record = {
        "employee_id": employee_id,
        "attendance_date": attendance_date,
        "status": "Present"
    }

    attendance_records.append(record)

    return {"status": "success", "record": record}