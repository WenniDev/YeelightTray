import sys
from pystray import MenuItem as item, Icon, Menu
import ctypes


class YeelightTray:    
    def __init__(self, config):
        self.config = config
        self.bulbs = config.bulbs
        self.app = Icon(
            config.name, 
            icon=config.icons["error"], 
            menu=None
        )

    def update_menu(self):
        bulb_items = [item(f'Toggle {bulb.name}', bulb.toggle) for bulb in self.bulbs]
        menu = Menu(
            item("Toggle light", self.toggle_all_bulbs, default=True, visible=False),
            item("Bulbs", Menu(*bulb_items)),
            item("Open configuration", self.open_config),
            item("Reload configuration", self.reload_config),
            item("Quit", self.quit_app)
        )
        self.app.menu = menu

    def add_bulb(self, bulb):
        if (bulb in self.bulbs):
            raise Exception("Bulb already exists")
        
        self.bulbs.append(bulb)
        self.update_icon()

    def remove_bulb(self, bulb):
        if (bulb not in self.bulbs):
            raise Exception("Bulb does not exist")
        self.bulbs.remove(bulb)
        self.update_icon()

    def toggle_single_bulb(self, bulb):
        bulb.toggle()
        self.update_icon()

    def toggle_all_bulbs(self):
        if len(self.bulbs) == 0:
            ctypes.windll.user32.MessageBoxW(0, "No bulbs found. Please open the configuration and add a light.", "Error", 1)
            self.open_config()
        try:
            state = self.get_room_state()
            for bulb in self.bulbs:
                if (state == "on"):
                    bulb.turn_off()
                else:
                    bulb.toggle()                
            self.update_icon()
        except Exception as e:
            print(f"Error toggling the bulb : {e}")

    def get_current_icon(self):
        if len(self.bulbs) == 0:
            return self.config.icons["error"]
        
        try:
            state = self.get_room_state()
            return self.config.icons[state]
        except Exception as e:
            print(f"Error updating the icon : {e}")

    def get_room_state(self):
        if len(self.bulbs) == 0:
            return "error"
        try:
            if any(bulb.is_on() for bulb in self.bulbs):
                return "on"
            return "off"
        except Exception as e:
            print(f"Cannot reach bulbs : {e}")

    def update_icon(self):
        self.app.icon = self.get_current_icon()

    def quit_app(self):
        self.app.stop()
        sys.exit()

    def open_config(self):
        self.config.openConfig()

    def reload_config(self):
        self.config.reloadConfig()
        self.config.parseConfig()
        self.bulbs = self.config.bulbs
        self.update_icon()
        self.update_menu()

    def run(self):
        try:
            self.update_icon()
            self.update_menu()
            self.app.run()
        except Exception as e:
            print(f"Error starting the app : {e}")