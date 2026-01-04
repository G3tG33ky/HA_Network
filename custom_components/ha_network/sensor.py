from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import EntityCategory

from .const import DOMAIN


class PcNetworkInfoSensor(SensorEntity):
    """Diagnostic sensor for static PC network information."""

    def __init__(self, entry, name: str, value: str, unique_id: str):
        self._entry = entry
        self._attr_name = f"{entry.data['name']} {name}"
        self._attr_native_value = value
        self._attr_unique_id = unique_id
        self._attr_entity_category = EntityCategory.DIAGNOSTIC

    @property
    def should_poll(self) -> bool:
        return False

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._entry.entry_id)},
            "name": self._entry.data["name"],
        }


async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities(
        [
            PcNetworkInfoSensor(
                entry,
                "IP Address",
                entry.data["ip_address"],
                f"{entry.entry_id}_ip",
            ),
            PcNetworkInfoSensor(
                entry,
                "MAC Address",
                entry.data["mac_address"],
                f"{entry.entry_id}_mac",
            ),
        ]
    )
