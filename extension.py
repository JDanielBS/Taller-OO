from enum import Enum


class Extension(Enum):
    TXT = ".txt"
    XML = ".xml"
    JSON = ".json"
    CSV = ".csv"

    @classmethod
    def getExtensionValues(cls):
        return [e.value for e in cls]