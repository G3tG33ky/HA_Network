import asyncio
import logging
from datetime import timedelta, datetime, timezone

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.core import HomeAssistant

from .const import DEFAULT_SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)


class HaNetworkCoordinator(DataUpdateCoordinator[bool]):
    def __init__(self, hass, ip_address: str):
        super().__init__(
            hass,
            logger=_LOGGER,
            name="ha_network",
            update_interval=timedelta(seconds=30),
        )

        self.ip_address = ip_address
        self.last_seen = None

    async def _ping(self) -> bool:
        try:
            process = await asyncio.create_subprocess_exec(
                "ping",
                "-c", "1",
                "-W", "1",
                self.ip_address,   
                stdout=asyncio.subprocess.DEVNULL,
                stderr=asyncio.subprocess.DEVNULL,
            )

            await process.communicate()
            return process.returncode == 0

        except Exception as err:
            _LOGGER.debug("Ping failed for %s: %s", self.ip_address, err)
            return False

    async def _async_update_data(self):
        online = await self._ping()

        if online:
            self.last_seen = datetime.now(timezone.utc)

        return {
            "online": online,
            "last_seen": self.last_seen,
        }
