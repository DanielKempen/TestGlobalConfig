from ConfigHandler import ConfigHandler
from ModelDeskExporter import ModelDeskExporter
from RestApiHandler import RestApiHandler

def uploadSkript():
    configHandler = ConfigHandler()
    configHandler.LoadConfigFromFile()
    config = configHandler.GetConfig()

    mockModelDeskExporter = ModelDeskExporter()
    mockModelDeskExporter.DoSomething()

    mockRestApiHanlder = RestApiHandler()
    mockRestApiHanlder.DoSomethingElse()
    print("Ende")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uploadSkript()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
