from datetime import datetime, timedelta

class Clock:
    """Interface/abstração sobre tempo usado pela aplicação."""
    def now(self) -> datetime:
        return datetime.utcnow()

class StubClock(Clock):
    def __init__(self, fixed_datetime):
        self._now = fixed_datetime

    def now(self) -> datetime:
        return self._now

    def shift_days(self, days: int):
        self._now = self._now + timedelta(days=days)
