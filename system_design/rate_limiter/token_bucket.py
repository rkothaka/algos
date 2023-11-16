import time


class TokenBucketRateLimiter:
    def __init__(self, max_tokens: int, tokens_per_second: float) -> None:
        self.max_tokens: int = max_tokens
        self.tokens: int = max_tokens
        self.tokens_per_second: float = tokens_per_second
        self.last_refresh_time = time.time()

    def _refresh_tokens(self) -> None:
        current_time = time.time()
        time_elapsed = current_time - self.last_refresh_time
        tokens_to_add = time_elapsed * self.tokens_per_second
        self.tokens = min(self.max_tokens, self.tokens + tokens_to_add)
        self.last_refresh_time = current_time

    def acquire(self, num_tokens=1) -> bool:
        if num_tokens <= 0:
            return True

        self._refresh_tokens()

        if self.tokens >= num_tokens:
            self.tokens -= num_tokens
            return True
        else:
            return False
