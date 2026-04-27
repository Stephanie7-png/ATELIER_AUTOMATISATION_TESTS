from tester.client import get_json

def test_status_200():
    res = get_json("/get/demo/key")
    return {
        "name": "HTTP status 200",
        "success": res["status_code"] == 200,
        "details": res
    }

def test_content_type_json():
    res = get_json("/get/demo/key")
    return {
        "name": "Content-Type JSON",
        "success": "application/json" in res["content_type"],
        "details": res
    }

def test_field_value_exists():
    res = get_json("/get/demo/key")
    data = res["json"]
    return {
        "name": "Champ obligatoire 'value' présent",
        "success": isinstance(data, dict) and "value" in data,
        "details": res
    }

def test_value_is_integer():
    res = get_json("/get/demo/key")
    data = res["json"]
    return {
        "name": "Le champ 'value' est un entier",
        "success": isinstance(data, dict) and isinstance(data.get("value"), int),
        "details": res
    }

def test_invalid_endpoint_404():
    res = get_json("/fake/demo/key")
    return {
        "name": "Endpoint invalide retourne 404",
        "success": res["status_code"] == 404,
        "details": res
    }

def test_latency_under_3_seconds():
    res = get_json("/get/demo/key")
    return {
        "name": "Latence inférieure à 3 secondes",
        "success": res["latency_ms"] is not None and res["latency_ms"] < 3000,
        "details": res
    }

def run_all_tests():
    return [
        test_status_200(),
        test_content_type_json(),
        test_field_value_exists(),
        test_value_is_integer(),
        test_invalid_endpoint_404(),
        test_latency_under_3_seconds()
    ]
