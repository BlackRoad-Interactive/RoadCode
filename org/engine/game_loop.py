"""Game loop — tick-based simulation for RoadWorld."""
import asyncio
import time
from dataclasses import dataclass

@dataclass
class GameState:
    tick: int = 0
    entities: int = 0
    fps: float = 0
    running: bool = False

class GameLoop:
    def __init__(self, tick_rate: int = 20):
        self.tick_rate = tick_rate
        self.state = GameState()

    async def run(self):
        self.state.running = True
        interval = 1.0 / self.tick_rate
        while self.state.running:
            start = time.monotonic()
            await self.update()
            self.state.tick += 1
            elapsed = time.monotonic() - start
            self.state.fps = 1.0 / max(elapsed, 0.001)
            await asyncio.sleep(max(0, interval - elapsed))

    async def update(self):
        pass  # Override in subclass

    def stop(self):
        self.state.running = False
