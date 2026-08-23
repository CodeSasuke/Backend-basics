"""Capacity-estimation starter."""


def estimate_requests_per_second(concurrency: int, average_latency_seconds: float) -> float:
    if concurrency < 1 or average_latency_seconds <= 0:
        raise ValueError("inputs must be positive")
    return concurrency / average_latency_seconds


if __name__ == "__main__":
    print(estimate_requests_per_second(concurrency=20, average_latency_seconds=0.2))
