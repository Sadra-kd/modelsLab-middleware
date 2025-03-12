from fastapi import APIRouter, HTTPException, Request
from app.services.request_forwarder import forward_request_to_modelslab

router = APIRouter()

@router.post("/proxy")
async def proxy_request(request: Request):
    """
    Receives a JSON request from Hooshex that contains:
      - "endpoint": the full URL to forward to,
      - Optionally "headers": the headers to forward,
      - And the payload data, either in a "body" key or as the remaining keys.
      
    The proxy will forward the payload to the given URL and return the response.
    """
    try:
        data = await request.json()
        endpoint = data.get("endpoint")
        if not endpoint:
            raise HTTPException(status_code=400, detail="Missing 'endpoint' field")

        # If a "body" key is provided, use its value as the payload;
        # otherwise, forward all keys except "endpoint"
        if "body" in data:
            payload = data["body"]
        else:
            payload = {k: v for k, v in data.items() if k != "endpoint"}

        # Get headers if provided; if not, default to an empty dictionary.
        headers = data.get("headers", {})

        response = forward_request_to_modelslab(endpoint, headers, payload)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
