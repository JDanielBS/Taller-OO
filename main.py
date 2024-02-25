from directory import Directory

route = input("Ingrese la ruta de la carpeta: ")
folder1 = Directory(route)

word = input("Ingrese la palabra a buscar: ")
folder1.searchWordInFolder(word)