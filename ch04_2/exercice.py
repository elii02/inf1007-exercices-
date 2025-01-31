#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_first_part_of_name(name):
	name = name.split("-")
	first_name= name[0]
	first_name = first_name[0].upper() + first_name[1:].lower()
	return "Bonjour " + first_name

def get_random_sentence(animals, adjectives, fruits):
	animaux = (chevreuil, chien, pigeon)
	adjectifs = (rouge, officiel, lourd) 
	fruits = (pommes, kiwis, bananes)

	return ""

def format_date(year, month, day, hours, minutes, seconds):
	return ""

def encrypt(text, shift):
	# car = "Z"
	# pas = 3
	# print((ord(car) - ord("A")+1 + pas) %26)

	phrase = "Allo"
	car = "Z"
	pas = 3
	chaine = ""
	for car in phrase: 
		if "A" <= car <= "Z":
			chaine += chr((ord(car) - ord("A") + pas) % 26 + ord("A"))
		elif "a" <= car <= "z":
			chaine += chr((ord(car) - ord("a") + pas) % 26 + ord("a"))
		else:
			chaine += car 
	print(chaine)
	return ""

def decrypt(encrypted_text, shift):
	return ""


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))

	print(format_date(1970, 1, 12, 12, 3, 45.6789))

	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
