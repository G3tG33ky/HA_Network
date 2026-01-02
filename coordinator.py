import asyncio
from datetime import timedelta

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.core import HomeAssistant

from .const import DEFAULT_SCAN_INTERVAL

async def async_ping(host: str) -> bool:
    proc = await asyncio.create_subprocess_exec(
        "ping", "-c", "1", "-W", "1", host,
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.DEVNULL,
    )
    await proc.communicate()
    return proc.returncode == 0

class PcNetworkCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, ip: str):
        super().__init__(
            hass,
            logger=None,
            name="PC Network Coordinator",
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )
        self.ip = ip

    async def _async_update_data(self):
        return await async_ping(self.ip)