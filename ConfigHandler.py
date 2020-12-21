from Config import Config

_Config = None

class ConfigHandler:

    def LoadConfigFromFile(self):
        fakeLoadedConfig = Config()
        fakeLoadedConfig.CredentialSet.Password = "default"
        fakeLoadedConfig.CredentialSet.UserName = "default"
        global _Config
        print(r'Hier wird das protected attribute "_Config" des moduls "ConfigHandler" gesetzt')
        _Config = fakeLoadedConfig
        pass

    def GetConfig(self):
        print("Module werden nur einmal geladen, im Gegensatz zu Klassen. Daher bleibt das protected attribute der Klasse ""_Config"" bestehen und kann hier geladen werden")
        return _Config



