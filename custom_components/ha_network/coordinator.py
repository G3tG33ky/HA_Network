import asyncio
import logging
from datetime import timedelta

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.core import HomeAssistant

from .const import DEFAULT_SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)


async def async_ping(host: str) -> bool:
    proc = await asyncio.create_subprocess_exec(
        "ping", "-c", "1", "-W", "1", host,
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.DEVNULL,
    )
    await proc.communicate()
    return proc.returncode == 0


class HaNetworkCoordinator(DataUpdateCoordinator[bool]):
    def __init__(self, hass: HomeAssistant, ip: str):
        super().__init__(
            hass,
            logger=_LOGGER,  # ✅ NIEMALS None
            name="HA Network Coordinator",
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )
        self.ip = ip

    async def _async_update_data(self):
        online = await self._ping()

        if online:
            self.last_seen = datetime.now(timezone.utc)

        return {
            "online": online,
            "last_seen": self.last_seen,
        }