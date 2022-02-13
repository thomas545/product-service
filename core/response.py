def response(data, message, status_code=200):
    return {
        "data": data,
        "code": status_code,
        "message": message,
        "length": len(data) if isinstance(data, list) else 0
    }


def error_response(error, message, code=400):
    return {"error": error, "code": code, "message": message}
