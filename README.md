# YeelightTray

`YeelightTray` is a software to manipulate Yeelight bulbs from the traybar.

# Installation

```shell
pip install pystray yeelight pyyaml toml Pillow
```

# Build

```shell
pyinstaller --onefile --noconsole --add-data ".\image\icon_error.png;image" --add-data ".\image\icon_off.png;image" --add-data ".\image\icon_on.png;image"  .\main.py
```

# Config example

```yaml
app:
  name: YeelightTray
bulbs:
  - address: 192.168.68.76
    name: Left Bulb

  - address: 192.168.68.77
    name: Right bulb
```

# Todo

- Add a graphic interface to add bulbs