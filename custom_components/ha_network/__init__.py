from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .coordinator import HaNetworkCoordinator

PLATFORMS = ["button", "binary_sensor"]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    coordinator = HaNetworkCoordinator(hass, entry.data["ip_address"])
    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = {
        "coordinator": coordinator,
        "entry": entry,
    }
    
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    sensors = [
        PcNetworkInfoSensor(
            coordinator,
            "IP Address",
            entry.data["ip"],
            f"{entry.entry_id}_ip",
        ),
        PcNetworkInfoSensor(
            coordinator,
            "MAC Address",
            entry.data["mac"],
            f"{entry.entry_id}_mac",
        ),
    ]

    hass.data[DOMAIN][entry.entry_id]["sensors"] = sensors
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    hass.data[DOMAIN].pop(entry.entry_id)
    return True


