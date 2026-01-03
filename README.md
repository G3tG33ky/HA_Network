# HA Network

A custom Home Assistant integration to control and monitor PCs on your local network.

**HA Network** provides:
- Wake-on-LAN functionality via a button entity
- Online/offline status via ICMP ping
- UI-based configuration (Config Flow)
- Support for multiple PCs
- HACS compatibility

---

## Features

- 🔌 **Wake-on-LAN**
  - Power on PCs remotely using a Home Assistant button
- 📡 **Online Status**
  - Binary sensor showing whether a PC is reachable via ping
- 🧩 **Config Flow**
  - Easy setup through the Home Assistant UI (no YAML required)
- 🖥️ **Multiple Devices**
  - Add and manage multiple PCs independently
- ⚡ **Async & Efficient**
  - Uses Home Assistant’s `DataUpdateCoordinator`
- 🧼 **Clean Integration**
  - Follows Home Assistant architecture and best practices

---

## Installation

### Option 1: HACS (Recommended)

1. Open **HACS**
2. Go to **Integrations**
3. Click **⋮ → Custom repositories**
4. Add this repository: https://github.com/G3tG33ky/ha_network
5. Select **Integration**
6. Install **HA Network**
7. Restart Home Assistant

---

### Option 2: Manual Installation

1. Copy the `ha_network` folder into: config/custom_components/
2. Restart Home Assistant

---

## Configuration

Configuration is done entirely via the Home Assistant UI.

1. Go to **Settings → Devices & Services**
2. Click **Add Integration**
3. Search for **HA Network**
4. Enter:
- **Name** – Display name of the PC
- **IP Address** – Local IP address of the PC
- **MAC Address** – MAC address of the network interface

Repeat these steps for each PC you want to add.

---

## Entities

For each configured PC, the integration creates:

### Button
- **`button.<pc_name>_wake`**
- Sends a Wake-on-LAN magic packet to the PC

### Binary Sensor
- **`binary_sensor.<pc_name>_online`**
- `on` → PC is reachable via ping  
- `off` → PC is offline or unreachable

---

## Requirements

- PC must be connected via **wired Ethernet**
- **Wake-on-LAN enabled** in:
- BIOS / UEFI
- Operating System
- Firewall must allow **ICMP (ping)**
- Home Assistant host must be on the same network

---

## Supported Platforms

- Linux
- Windows
- macOS  
(As long as Wake-on-LAN and ICMP are supported)

---

## Troubleshooting

### Wake-on-LAN does not work
- Verify MAC address
- Check BIOS/UEFI power settings
- Ensure the PC supports WoL from S5/S4 state
- Use wired Ethernet (Wi-Fi WoL is often unsupported)

### PC always shows offline
- Ensure ping is allowed by the firewall
- Verify IP address
- Check network isolation / VLAN settings

---

## Roadmap

- Device registry support
- Device tracker entity
- Broadcast address configuration
- Automatic network discovery
- Additional translations
- Unit tests & CI validation

---
## Wake-on-LAN Setup (Important)

Wake-on-LAN requires proper configuration on the target PC.  
If the PC does not start when pressing the wake button, please verify the following steps carefully.

---

### BIOS / UEFI Configuration (Required)

Enter the BIOS/UEFI settings of the PC and ensure the following options are enabled  
(option names vary by manufacturer):

- **Wake on LAN**
- **Power On by PCI-E**
- **Resume by LAN**
- **Wake from S5 / Soft Off**

Disable the following option if present:

- **ErP / EuP Mode** (very common cause of Wake-on-LAN failure)

> Tip:  
> This option is often found under  
> **Advanced → Power Management**

---

### Windows Configuration

#### Network Adapter – Power Management

1. Open **Device Manager**
2. Navigate to **Network Adapters**
3. Open your **wired Ethernet adapter**
4. Go to **Power Management**

Enable the following options:

- Allow this device to wake the computer
- Only allow a magic packet to wake the computer

---

#### Network Adapter – Advanced Settings

In the **Advanced** tab of the same adapter, enable options such as:

- **Wake on Magic Packet**
- **Wake on Pattern Match**
- **Shutdown Wake-On-LAN**
- **Wake from Power Off**

(The exact names depend on the network driver.)

---

#### Disable Windows Fast Startup (Very Important)

Windows Fast Startup often prevents Wake-on-LAN from working correctly.

1. Open **Control Panel**
2. Go to **Power Options**
3. Click **Choose what the power buttons do**
4. Click **Change settings that are currently unavailable**
5. Disable:
   - **Turn on fast startup**
6. Reboot the PC

---

### Linux Configuration

Check if Wake-on-LAN is enabled:

```bash
ethtool eth0
```

---

## Contributions

Contributions are welcome!  
Please follow Home Assistant development guidelines and open a pull request.

---

## License

MIT License
Copyright (c) 2026 Julian Bludau

Permission is hereby granted, free of charge, to any person obtaining a copy
---

## Disclaimer

This project is not affiliated with or endorsed by the Home Assistant project.
