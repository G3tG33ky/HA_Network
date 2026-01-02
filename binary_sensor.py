from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, MANUFACTURER, MODEL

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]["coordinator"]
    async_add_entities([PcOnlineSensor(entry, coordinator)])

class PcOnlineSensor(CoordinatorEntity, BinarySensorEntity):
    def __init__(self, entry, coordinator):
        super().__init__(coordinator)
        self._entry = entry
        self._attr_name = f"{entry.data['name']} Online"
        self._attr_unique_id = f"{entry.entry_id}_online"
        self._attr_device_class = "connectivity"

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._entry.entry_id)},
            "name": self._entry.data["name"],
            "manufacturer": MANUFACTURER,
            "model": MODEL,
        }

    @property
    def is_on(self):
        return self.coordinator.data