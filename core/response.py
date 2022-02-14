from fastapi import HTTPException

def response(data, message, status_code=200):
    return {
        "data": data,
        "code": status_code,
        "message": message,
        "length": len(data) if isinstance(data, list) else 0
    }


def error_response(message, code=400):
    raise HTTPException(code, message)
