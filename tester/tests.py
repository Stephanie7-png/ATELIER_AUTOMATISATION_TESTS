from tester.client import get_json

def test_status_200():
    res = get_json("/?format=json")
    return {
        "name": "HTTP status 200",
        "success": res["status_code"] == 200,
        "details": res
    }

def test_content_type_json():
    res = get_json("/?format=json")
    return {
        "name": "Content-Type JSON",
        "success": "application/json" in res["content_type"],
        "details": res
    }

def test_field_ip_exists():
    res = get_json("/?format=json")
    data = res["json"]

    return {
        "name": "Champ ip présent",
        "success": isinstance(data, dict) and "ip" in data,
        "details": res
    }

def test_ip_is_string():
    res = get_json("/?format=json")
    data = res["json"]

    return {
        "name": "Champ ip est string",
        "success": isinstance(data, dict) and isinstance(data.get("ip"), str),
        "details": res
    }

def test_latency_under_3s():
    res = get_json("/?format=json")

    return {
        "name": "Latence < 3 sec",
        "success": res["latency_ms"] is not None and res["latency_ms"] < 3000,
        "details": res
    }

def test_invalid_endpoint():
    res = get_json("/fake")

    return {
        "name": "Endpoint invalide",
        "success": res["status_code"] in [400, 404],
        "details": res
    }

def run_all_tests():
    return [
        test_status_200(),
        test_content_type_json(),
        test_field_ip_exists(),
        test_ip_is_string(),
        test_latency_under_3s(),
        test_invalid_endpoint()
    ]
