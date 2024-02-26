import os
import re
import xml.etree.ElementTree as ET
import json
import csv
from extension import Extension


class File():
    def __init__(self, filename, route):
        self._filename = filename
        self.__fileroute = route+'/'+filename
        self._words = 0
            
    def countWords(self, word):
        with open(self.__fileroute, 'r') as file:
            ext = os.path.splitext(self._filename)[1]
            if ext == Extension.TXT.value:
                content = file.read()
                self._words = len(re.findall(r'\b{}\b'.format(word), content))
            elif ext == Extension.XML.value:
                tree = ET.parse(self.__fileroute)
                content = ET.tostring(tree.getroot(), encoding='utf8').decode('utf8')
                self._words = len(re.findall(r'\b{}\b'.format(word), content))
            elif ext == Extension.JSON.value:
                data = json.load(file)
                content = json.dumps(data)
                self._words = len(re.findall(r'\b{}\b'.format(word), content))
            elif ext == Extension.CSV.value:
                reader = csv.reader(file)
                for row in reader:
                    count += len(re.findall(r'\b{}\b'.format(word), ' '.join(row)))
