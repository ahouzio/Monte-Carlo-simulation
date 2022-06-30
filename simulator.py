#!/usr/bin/env python3
"""Ce programme donne une approximation du nombre pi à l'aide de la
                    méthode de Monte Carlo"""

import random as rd
from collections import namedtuple
import sys

def point(x, y):
    """Crée un objet point."""
    Point = namedtuple("Point", 'x y')
    return Point(x, y)
  
def cercle(centre, rayon):
    """Crée un objet cercle."""
    Cercle = namedtuple("cercle", 'centre rayon')
    return Cercle(centre, rayon)
  
def distance(pt1, pt2):
    """Calcule la distance entre deux points du plan."""
    return ((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)**(0.5)
  
def interieur_cercle(circle, pointe):
    """Check si un point est bien à l'intérieur d'un cercle donné"""
    return True if distance(circle[0], pointe) <= circle[1] else False
  
def generateur_points(nbr_points):
    """Genere nbr_points aléatoire dans un carré de coté 1."""
    for _ in range(nbr_points):
        candidat = point(rd.uniform(-1, 1), rd.uniform(-1, 1))
        yield candidat
        
def main(nombre_de_points):
    """La fonction principale"""
    nombre_de_points = int(nombre_de_points)
    points_cercle = 0
    point_origine = point(0, 0)
    cercle_unite = cercle(point_origine, 1)
    for candidat in generateur_points(nombre_de_points):
        if interieur_cercle(cercle_unite, candidat):
            points_cercle += 1
    approx_pi = 4 * (points_cercle/nombre_de_points)
    return approx_pi
  
if __name__ == "__main__":
    print(main(sys.argv[1]))
