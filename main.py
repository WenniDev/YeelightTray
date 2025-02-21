from YeelightTray import YeelightTray
from YeelightConfig import YeelightConfig

import sys 
import os

config_path = os.path.join(os.getenv('LOCALAPPDATA'), 'YeelighTray', 'config.yaml')

def main():
    config = YeelightConfig(config_path, is_yaml=True)
    config.parseConfig()
    tray = YeelightTray(config=config)
    tray.run()

if __name__ == "__main__":
    main()
    sys.exit(0)