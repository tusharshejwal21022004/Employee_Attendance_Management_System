def login(username, password):
    if username == "employee1" and password == "pass":
        return {"status": "success", "token": "mock-jwt-token"}

    return {"status": "failed"}