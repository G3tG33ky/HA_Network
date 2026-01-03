from homeassistant.components.sensor import SensorEntity
from homeassistant.const import EntityCategory

class PcNetworkInfoSensor(SensorEntity):
    """Diagnostic sensor for static PC network information."""

    def __init__(self, coordinator, name, value, unique_id):
        self.coordinator = coordinator
        self._attr_name = name
        self._attr_native_value = value
        self._attr_unique_id = unique_id
        self._attr_entity_category = EntityCategory.DIAGNOSTIC

    @property
    def should_poll(self):
        return False

    async def async_update(self):
        return