import os
from extension import Extension
from file import File

class Directory():
    def __init__(self, route):
        self.route = route
        self.files = []
        self.searchFolder(route)
        self.totalWords = 0

    def searchFolder(self, route):
        if os.path.isdir(route):
            for file in os.listdir(route):
                if os.path.splitext(file)[1] in Extension.getExtensionValues():
                    self.files.append(File(file, route))
        else:
            print("No se encuentra la carpeta indicada")

    def searchWordInFolder(self, word):
        if self.files != []:
            for file in self.files:
                file.countWords(word)
                self.totalWords += file.words
            self.showFiles()
        elif self.files == [] and os.path.isdir(self.route) == True:
            print("No hay archivos de texto en la carpeta")
            

    def showFiles(self):
        for file in self.files:
            print(f"{file.filename}: {file.words} veces")
        print(f"Total: {self.totalWords}")

carpeta1 = Directory("C:/Users/Daniel/Downloads/T. Universidad/Semestre V/Ingeniería de software/Taller OO/prueba1")