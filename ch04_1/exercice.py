#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    chaine = "hello"
    print("Chaine a un nrb pair" if len(chaine)%2 ==0 else "Chaine a un nbr impair")
    pass


def remove_third_char(string: str) -> str:
    chaine = "hello"
    print(chaine[:2] + chaine[3:])
    pass


def replace_char(string: str, old_char: str, new_char: str) -> str:
    chaine='hello'
    print(chaine.replace("o", "a"))
    # chaine='hello'
    # pos1 = chaine.find("o")
    # print(chaine[:pos1] + "a" + chaine[:pos1 +1 :] )
    # pos1 = chaine.rfind("o")
    # print(chaine[:pos1] + "a" + chaine[:pos1 +1 :] )
    pass


def get_number_of_char(string: str, char: str) -> int:
    chaine='hello'
    for car in chaine:
        print(car)
    # for i in range(len(chaine)):
    #     print(i, chaine[1])
    # for i, car in enumerate(chaine, 10):
    #     print(i, car)
    pass


def get_number_of_words(sentence: str, word: str) -> int:
    paragraphe = """ Lorem ha ha je suis la plus belle hihi ou hi"""
    print(len(paragraphe.split()))
    pass


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans {chaine} est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
