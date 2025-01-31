#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
import math


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number = number*-1
        return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    chaine = ""
    for indice, car in enumerate(prefixes):
        chaine += car + suffixe + (", " if indice < len(prefixes)-1 else"")
    return chaine


def prime_integer_summation() -> int:
    nombre = 2
    compteur = 0
    somme = 0
    while compteur < 100:
        for i in range(2, int(math.sqrt(nombre) +1)):
            if nombre % i == 0:
                break
        else: #close else de la boucle for
            compteur += 1 
            somme += nombre
        nombre +=1
    return compteur, somme


def factorial(number: int) -> int:
    nombre = 0
    resultat = nombre if nombre != 0 else 1
    for i in range(2, nombre):
        resultat *= i 
    return resultat


def use_continue() -> None:
    for i in range(1,11):
        if i == 5:
            continue
        
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    return []


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
