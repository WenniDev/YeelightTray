from yeelight import Bulb, LightType

class YeelightBulb(Bulb):
    def __init__(self, address, name):
        super().__init__(address)
        self.name = name
        self.address = address
    
    def turn_on(self, light_type=LightType.Main, **kwargs):
        try:
            return super().turn_on(light_type, **kwargs)
        except Exception as e:
            print(f"Error turning on the bulb : {e}")

    def turn_off(self, light_type=LightType.Main, **kwargs):
        try:
            return super().turn_off(light_type, **kwargs)
        except Exception as e:
            print(f"Error turning off the bulb : {e}")

    def toggle(self, light_type=LightType.Main, **kwargs):
        try:
            return super().toggle(light_type, **kwargs)
        except Exception as e:
            print(f"Error toggling the bulb : {e}")

    def set_brightness(self, brightness, light_type=LightType.Main, **kwargs):
        try:
            return super().set_brightness(brightness, light_type, **kwargs)
        except Exception as e:
            print(f"Error editing the brightness : {e}")

    def get_status(self):
        try:
            return super().get_properties()["power"]
        except Exception as e:
            print(f"Cannot reach the bulb : {e}")

    def is_on(self):
        try:
            return self.get_status() == "on"
        except Exception as e:
            print(f"Cannot reach the bulb : {e}")
            return False
    