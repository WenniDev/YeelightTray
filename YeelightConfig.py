from YeelightBulb import YeelightBulb
from PIL import Image
import os
import sys
import subprocess

import json
import yaml
import toml

class YeelightConfig:
    def __init__(self, target_file, is_json=False, is_yaml=False, is_toml=False):
        self.file = target_file
        
        self.application = []
        
        self.is_json = is_json
        self.is_yaml = is_yaml
        self.is_toml = is_toml

        if not os.path.exists(self.file):
            self.createConfig()

        if is_json:
            self.loadJsonConfig()
        elif is_yaml:
            self.loadYamlConfig()
        elif is_toml:
            self.loadTomlConfig()

    def loadYamlConfig(self):
        with open(self.file, 'r') as file:
            self.config = yaml.safe_load(file)

    def loadJsonConfig(self):
        with open(self.file, 'r') as file:
            self.config = json.load(file)

    def loadTomlConfig(self):
        with open(self.file, 'r') as file:
            self.config = toml.load(file)

    def openConfig(self):
        if sys.platform == 'win32':
            os.startfile(self.file)
        elif sys.platform == 'darwin':
            subprocess.Popen(['open', self.file])
        else:
            subprocess.Popen(['xdg-open', self.file])

    def addBulbs(self, name, address):
        for bulb in self.bulbs:
            if bulb.address == address:
                return
        
        self.bulbs.append(YeelightBulb(name=name, address=address))

    def removeBulbs(self, address):
        for bulb in self.bulbs:
            if bulb.address == address:
                self.bulbs.remove(bulb)

    def reloadConfig(self):
        if self.is_json:
            self.loadJsonConfig()
        elif self.is_yaml:
            self.loadYamlConfig()
        elif self.is_toml:
            self.loadTomlConfig()

    def getResourcePath(self, relative_path):
        """ Récupère le bon chemin des fichiers intégrés dans l'exécutable """
        if getattr(sys, 'frozen', False):  # Exécutable
            base_path = sys._MEIPASS
        else:  # Mode normal
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
    def parseConfig(self):
        self.bulbs = []
        self.icons = {}
        self.name = self.config['app']['name']
        if 'bulbs' in self.config:
            for bulb in self.config['bulbs']:
                self.bulbs.append(YeelightBulb(bulb['address'], bulb['name']))
        self.icons["error"] = Image.open(self.getResourcePath("image/icon_error.png"))
        self.icons["on"] = Image.open(self.getResourcePath("image/icon_on.png"))
        self.icons["off"] = Image.open(self.getResourcePath("image/icon_off.png"))


    def writeToJson(self, config):
        with open(self.file, 'w') as file:
            json.dump(config, file, indent=4)

    def writeToYaml(self, config):
        with open(self.file, 'w') as file:
            yaml.dump(config, file)
    
    def writeToToml(self, config):
        with open(self.file, 'w') as file:
            toml.dump(config, file)

    def createConfig(self):
        config = {
            'app': {
                'name': "YeelightTray"
            },
        }

        os.makedirs(os.path.dirname(self.file), exist_ok=True)
        if self.is_json:
            self.writeToJson(config)
        elif self.is_yaml:
            self.writeToYaml(config)
        elif self.is_toml:
            self.writeToToml(config)

    def __str__(self):
        return f"Name: {self.name}\nBulbs: {self.bulbs}\nIcons: {self.icons}"