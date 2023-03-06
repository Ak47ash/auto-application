from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

API_AUTH_KEY = "x-api-key"
api_key_header_obj = APIKeyHeader(name=API_AUTH_KEY, auto_error=False)


USERS = {
    # Internal usage
    "3UC9lFLG7UdCFpbAEZeyIlxlke1Xn": "global",
    "akash": "Akash",
    "aniket": "Aniket",
    "shubham": "Shubham",
    "vikas": "Vikas"
}


async def get_api_key(api_key_header: str = Security(api_key_header_obj)):
    if api_key_header in USERS:
        return USERS[api_key_header]
    else:
        raise HTTPException(
            status_code=403,
            detail={"state": "error", "message": "Invalid or missing auth key."},
        )