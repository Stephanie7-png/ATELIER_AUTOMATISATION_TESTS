import time
import requests

BASE_URL = "https://api.countapi.xyz"

def get_json(endpoint, timeout=3, retry=1):
    url = BASE_URL + endpoint

    for attempt in range(retry + 1):
        start = time.time()

        try:
            response = requests.get(url, timeout=timeout)
            latency_ms = round((time.time() - start) * 1000, 2)

            try:
                json_data = response.json()
            except ValueError:
                json_data = None

            return {
                "url": url,
                "status_code": response.status_code,
                "content_type": response.headers.get("Content-Type", ""),
                "json": json_data,
                "latency_ms": latency_ms,
                "error": None
            }

        except requests.exceptions.RequestException as e:
            if attempt == retry:
                return {
                    "url": url,
                    "status_code": None,
                    "content_type": "",
                    "json": None,
                    "latency_ms": None,
                    "error": str(e)
                }
