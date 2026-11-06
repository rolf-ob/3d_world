import time
from collections import deque

class FrameLimiter:
    def __init__(self):
        self.frame_times = deque()
        self.last_frame = time.perf_counter()

    def limit_fps(self, target_fps):
        remaining_time = time.perf_counter() - self.last_frame - 0.0005

        if remaining_time > 0.001:
            time.sleep(remaining_time)

        while remaining_time > time.perf_counter():
            pass

        self.last_frame = time.perf_counter()

    def tick(self):
        now = time.perf_counter()
        self.frame_times.append(now)

        while self.frame_times[-1] + 1 <= now:
            self.frame_times.popleft()

    def get_fps(self):
        return len(self.frame_times)