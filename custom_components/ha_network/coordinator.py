import asyncio
import logging
from datetime import timedelta, datetime, timezone

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.core import HomeAssistant

from .const import DEFAULT_SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)


class HaNetworkCoordinator(DataUpdateCoordinator[bool]):
    def __init__(self, hass: HomeAssistant, ip: str):
        super().__init__(
            hass,
            logger=_LOGGER,  # ✅ NIEMALS None
            name="HA Network Coordinator",
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )
        self.ip = ip

    async def _ping(self) -> bool:
        proc = await asyncio.create_subprocess_exec(
            "ping", "-c", "1", "-W", "1", self.ip,
            stdout=asyncio.subprocess.DEVNULL,
            stderr=asyncio.subprocess.DEVNULL,
        )
        await proc.communicate()
        return proc.returncode == 0

    async def _async_update_data(self):
        online = await self._ping()

        if online:
            self.last_seen = datetime.now(timezone.utc)

        return {
            "online": online,
            "last_seen": self.last_seen,
        }
