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
            print(f"Erreur lors de l'allumage de l'ampoule : {e}")

    def turn_off(self, light_type=LightType.Main, **kwargs):
        try:
            return super().turn_off(light_type, **kwargs)
        except Exception as e:
            print(f"Erreur lors de l'arrêt de l'ampoule : {e}")

    def toggle(self, light_type=LightType.Main, **kwargs):
        try:
            return super().toggle(light_type, **kwargs)
        except Exception as e:
            print(f"Erreur lors du basculement de l'ampoule : {e}")

    def set_brightness(self, brightness, light_type=LightType.Main, **kwargs):
        try:
            return super().set_brightness(brightness, light_type, **kwargs)
        except Exception as e:
            print(f"Erreur lors du réglage de la luminosité : {e}")

    def get_status(self):
        try:
            return super().get_properties()["power"]
        except Exception as e:
            print(f"Erreur lors de la récupération de l'état de l'ampoule : {e}")

    def is_on(self):
        try:
            return self.get_status() == "on"
        except Exception as e:
            print(f"Erreur lors de la vérification de l'état de l'ampoule : {e}")
            return False
    