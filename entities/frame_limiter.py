import time
from collections import deque

class FrameLimiter:
    def __init__(self):
        self.frame_times = deque()
        self.next_frame = time.perf_counter()

    def limit_fps(self, target_fps: int) -> None:
        remaining_time = self.next_frame - time.perf_counter() - 0.0005

        if remaining_time > 0.001:
            time.sleep(remaining_time)

        while time.perf_counter() < self.next_frame:
            pass

        self.next_frame = time.perf_counter() + 1 / target_fps

    def tick(self) -> None:
        now = time.perf_counter()
        self.frame_times.append(now)

        while self.frame_times[-1] + 1 <= now:
            self.frame_times.popleft()

    def get_fps(self) -> int:
        return len(self.frame_times)