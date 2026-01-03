from homeassistant.components.button import ButtonEntity
from wakeonlan import send_magic_packet

from .const import DOMAIN, MANUFACTURER, MODEL

async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([WakePcButton(entry)])

class WakePcButton(ButtonEntity):
    def __init__(self, entry):
        self._entry = entry
        self._attr_name = f"{entry.data['name']} Wake"
        self._attr_unique_id = f"{entry.entry_id}_wake"
        self._mac = entry.data["mac_address"]

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._entry.entry_id)},
            "name": self._entry.data["name"],
            "manufacturer": MANUFACTURER,
            "model": MODEL,
        }

    def press(self):
        send_magic_packet(self._mac)