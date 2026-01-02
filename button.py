from homeassistant.components.button import ButtonEntity
from wakeonlan import send_magic_packet

from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    data = hass.data[DOMAIN][entry.entry_id]["data"]
    async_add_entities([WakePcButton(data)])

class WakePcButton(ButtonEntity):
    def __init__(self, data):
        self._attr_name = f"{data['name']} Wake"
        self._mac = data["mac_address"]

    def press(self):
        send_magic_packet(self._mac)