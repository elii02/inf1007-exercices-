#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def square_root(a: float) -> float:
    return math.sqrt(a)


def square(a: float) -> float:
    return math.pow(a,2)


def average(a: float, b: float, c: float) -> float:
    return (sum([a,b,c]))/3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    return (angle_degs+ (angle_mins + (angle_secs/60))/60) *math.pi/180


def to_degrees(angle_rads: float) -> tuple:
    deg_dec = angle_rads *180/math.pi
    angle_degs, reste = divmod(deg_dec, 1)
    angle_mins, angle_secs = 3,4
    return deg_dec, angle_degs, angle_mins


def to_celsius(temperature: float) -> float:
    return (temperature-32)/1.8


def to_farenheit(temperature: float) -> float:
    return temperature*1.8 + 32


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")

    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
