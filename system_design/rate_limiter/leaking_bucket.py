import time
import collections


class LeakyBucketRateLimiter:
    def __init__(self, bucket_size, rate_limit_per_second):
        self.bucket = collections.deque(maxlen=bucket_size)
        self.rate_limit_per_second = rate_limit_per_second
        self.last_leak_time = time.time()

    def _leak(self):
        current_time = time.time()
        time_elapsed = current_time - self.last_leak_time
        tokens_to_add = time_elapsed * self.rate_limit_per_second

        # Add tokens to the bucket
        for _ in range(min(int(tokens_to_add), len(self.bucket))):
            self.bucket.popleft()

        self.last_leak_time = current_time

    def allow_request(self):
        self._leak()

        if len(self.bucket) < self.bucket.maxlen:
            self.bucket.append(time.time())
            return True
        else:
            return False

