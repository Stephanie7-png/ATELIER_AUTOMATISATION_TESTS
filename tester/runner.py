from tester.tests import run_all_tests

def run_tests():
    results = run_all_tests()

    total = len(results)
    passed = sum(1 for test in results if test["success"])
    failed = total - passed

    latencies = [
        test["details"]["latency_ms"]
        for test in results
        if test["details"]["latency_ms"] is not None
    ]

    avg_latency = round(sum(latencies) / len(latencies), 2) if latencies else 0
    max_latency = max(latencies) if latencies else 0
    success_rate = round((passed / total) * 100, 2)

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "success_rate": success_rate,
        "avg_latency": avg_latency,
        "p95_latency": max_latency,
        "results": results
    }
