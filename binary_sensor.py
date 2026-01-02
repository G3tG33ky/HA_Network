from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]["coordinator"]
    name = hass.data[DOMAIN][entry.entry_id]["data"]["name"]

    async_add_entities([PcOnlineSensor(coordinator, name)])

class PcOnlineSensor(CoordinatorEntity, BinarySensorEntity):
    def __init__(self, coordinator, name):
        super().__init__(coordinator)
        self._attr_name = f"{name} Online"
        self._attr_device_class = "connectivity"

    @property
    def is_on(self):
        return self.coordinator.data