import csv

def dict(fichier):
    with open(fichier, 'r') as file:
        file_read = file.readlines()
        print(file_read)


dict("ventes.txt")