import os
from extension import Extension
from file import File

class Directory():
    def __init__(self, route):
        self.__route = route
        self.__files = []
        self.searchFolder(route)
        self.__totalWords = 0

    def searchFolder(self, route):
        if os.path.isdir(route):
            for file in os.listdir(route):
                if os.path.splitext(file)[1] in Extension.getExtensionValues():
                    self.__files.append(File(file, route))
        else:
            print("No se encuentra la carpeta indicada")

    def searchWordInFolder(self, word):
        if self.__files != []:
            for file in self.__files:
                file.countWords(word)
                self.__totalWords += file._words
            self.showFiles()
        elif self.__files == [] and os.path.isdir(self.__route) == True:
            print("No hay archivos de texto en la carpeta")
            

    def showFiles(self):
        for file in self.__files:
            print(f"{file._filename}: {file._words} veces")
        print(f"Total: {self.__totalWords}")
