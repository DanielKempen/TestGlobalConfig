from ConfigHandler import ConfigHandler
class RestApiHandler:
    def __init__(self):
        pass

    def DoSomethingElse(self):
        configHandler = ConfigHandler()
        config = configHandler.GetConfig()
        print("auch hier wird die config des handler verwendet, ohne sie vorherh übergeben zu müssen")
