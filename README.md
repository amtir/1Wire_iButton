# 1-Wire iButton Reader — Raspberry Pi

A Python 3 program that reads the unique serial number of **Dallas / Maxim iButtons** (e.g. DS1990A) over the **1-Wire** bus on a Raspberry Pi, for **automatic identification** such as access control, user login or time tracking.

<p align="center">
  <img src="photos/iButton-1Wire_Dallas.png" alt="iButton reader and keys" width="420">
</p>

## Background

**1-Wire** is a communication bus designed by Dallas Semiconductor. It carries low-speed data (16.3 kbps), signalling and power over a single conductor, so a device needs only two wires: data and ground.

Every 1-Wire chip has a factory-programmed, globally unique **64-bit ID** (8-bit family code + 48-bit serial + 8-bit CRC). This makes iButtons practical electronic keys for locks, alarms, computer systems, accessories and time clocks. [More on Wikipedia](https://en.wikipedia.org/wiki/1-Wire).

## How It Works

1. Loads the Linux 1-Wire kernel drivers (`w1-gpio`, `w1-smem`). The bus is on **GPIO 4** by default.
2. Polls `/sys/devices/w1_bus_master1/w1_master_slaves` for a connected iButton.
3. Prints the ID with a timestamp as soon as a key touches the reader.
4. Writes the ID to `w1_master_remove` so the next touch is detected right away.

> By default the kernel scans the bus only every 10 s. For an instant response, lower the timeout, e.g. `w1_master_timeout=0`, `w1_master_timeout_us=500` (see the comments in the script).

## Hardware

| Component | Connection |
|-----------|------------|
| Raspberry Pi | Raspbian / Raspberry Pi OS |
| iButton probe (reader) | Data → **GPIO 4**, Ground → GND |
| Pull-up resistor | ~4.7 kΩ between data and 3.3 V |
| iButtons | DS1990A (family code `01`) or compatible |

<p align="center">
  <img src="photos/iButton_Dallas.jpeg" alt="iButton keys" width="380">
</p>

## Getting Started

```bash
# Enable the 1-Wire interface
echo "dtoverlay=w1-gpio" | sudo tee -a /boot/config.txt
sudo reboot

pip3 install -r requirements.txt
sudo python3 src/iButton-1Wire.py
```

## Sample Output

```
2019-06-07T16:45:15.076385 : iButton-ID = 01-0000XXXXXXXX
2019-06-07T16:45:15.135908 : iButton-ID = 01-0000XXXXXXXX
```

`01` is the family code (DS1990A). IDs are masked here; a full run is in [`logs/sample_output.txt`](logs/sample_output.txt).

## Repository Structure

```
.
├── src/iButton-1Wire.py   # Reader program
├── logs/                  # Sample run output
├── photos/                # Reader and key photos
└── requirements.txt
```

## Tech Stack

Python 3 · Raspberry Pi · 1-Wire (w1-gpio) · Linux sysfs · Dallas / Maxim iButton

## Author

**Akram M'Tir**, [@amtir](https://github.com/amtir)
