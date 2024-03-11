import os
from configparser import ConfigParser

from src.commons.constants.constants import ConfigConstants


class ConfigClient:

    @staticmethod
    def get_property(section: str, name: str):
        try:
            env = os.environ.get("env")
            config = ConfigParser()
            path = os.getcwd() + ConfigConstants.PATH.format(env=env)
            config.read(path)

            value = config.get(section, name)
            return value
        except (FileNotFoundError, KeyError) as e:
            # Handle exceptions related to reading the .ini file
            print(f"An error occurred while reading the config file: {e}")
            return None
        except Exception as e:
            # Handle other unexpected exceptions
            print(f"An unexpected error occurred: {e}")
            return None

    @staticmethod
    def get_boolean_property(section: str, name: str):
        try:
            env = os.environ.get("env")
            config = ConfigParser()
            path = os.getcwd() + ConfigConstants.PATH.format(env=env)
            config.read(path)

            value = config.getboolean(section, name)
            return value
        except (FileNotFoundError, KeyError) as e:
            # Handle exceptions related to reading the .ini file
            print(f"An error occurred while reading the config file: {e}")
            return None
        except Exception as e:
            # Handle other unexpected exceptions
            print(f"An unexpected error occurred: {e}")
            return None

