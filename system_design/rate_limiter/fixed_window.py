import time


class FixedWindowRateLimiter:
    def __init__(self, max_requests, window_duration):
        self.max_requests = max_requests
        self.window_duration = window_duration
        self.window_start_time = time.time()
        self.window_requests = 0

    def _reset_window(self):
        self.window_start_time = time.time()
        self.window_requests = 0

    def allow_request(self):
        current_time = time.time()

        # Check if the current window has expired
        if current_time - self.window_start_time > self.window_duration:
            self._reset_window()

        if self.window_requests < self.max_requests:
            self.window_requests += 1
            return True
        else:
            return False
