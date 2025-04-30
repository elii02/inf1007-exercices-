import csv

def dictt(fichier):
    with open(fichier, 'r') as file:
        
        # Read file
        file_read = file.readlines()
        print(file_read)

        # Create new list for clean data (lists in list)
        new_list = []
        for element in file_read:
            e = element.replace(';', '').strip().split()
            new_list.append(e)
        print(new_list)

        # Put into dict 
        dict_pd = {}
        for list in new_list:
            dict_pd[list[0]] = { "Premier tri": int(list[1]), "Deuxieme tri": int(list[2]), "Troisieme tri": int(list[3]), "Deck": (list[4])}
        print(dict_pd)
        return dict_pd



def export_csv(dict_pd, fichier_csv):
    with open(fichier_csv, 'w') as file_csv:
        written = file_csv.write(dict_pd)



dictt("ventes.txt")     
