import os

settings = None
projectPath = None
environment = None
config = None


def load_settings():

    """
        This function is to load the settings file
    """
    global projectPath
    projectPath = os.path.dirname(os.path.dirname(os.path.expanduser(__file__)))

load_settings()
