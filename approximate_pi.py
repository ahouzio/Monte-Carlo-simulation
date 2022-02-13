#!/usr/bin/env python3
"""Ce module cree une image gif contenant des images ppm donnant une
approximation pi en format texte au milieu de l'image"""
import time
import array
import sys
import subprocess
import simulator as sim
START_TIME = time.time()
if len(sys.argv) != 4:
    raise ValueError("Respectez le format suivant: (fonction taille nombre_de_points précision)")
TAILLE = sys.argv[1]
NBR_POINTS = sys.argv[2]
PRECISION = sys.argv[3]
if not(TAILLE.isdigit() and NBR_POINTS.isdigit() and PRECISION.isdigit()):
    raise ValueError("Entrer des arguments entier positifs")
TAILLE = int(TAILLE)
NBR_POINTS = int(NBR_POINTS)
PRECISION = int(PRECISION)
nbr_point = int(NBR_POINTS/10)
if TAILLE <= 0 or NBR_POINTS <= 0:
    raise ValueError("Entrez une taille ou un nombre de points strictement positifs")
if PRECISION < 0:
    raise ValueError("Entrez une précision positif")
POINTS_CERCLE = 0
MAX_VAL = 255
PPM_HEADER = f'P6 {TAILLE} {TAILLE} {MAX_VAL}\n'
IMAGE = array.array('B', [255, 255, 255] * TAILLE * TAILLE)
POINT_ORIGINE = sim.point(0, 0)
CERCLE_UNITE = sim.cercle(POINT_ORIGINE, 1)
INDEX_CHIFFRE = [] #sauvegarde les positions des pixels des chiffres tracés
def trait_vertical(point_depart, longueur, direction):
    """Dessine un trait vertical noir."""
    x, y = int(point_depart[0]), int(point_depart[1])
    if direction == "bas":
        for i in range(longueur):
            index1 = 3 * ((y + i) * TAILLE +x)
            index2 = index1 +3
            INDEX_CHIFFRE.append(index1)
            INDEX_CHIFFRE.append(index2)
            IMAGE[index2], IMAGE[index2+1], IMAGE[index2+2] = 0, 0, 0
            IMAGE[index1], IMAGE[index1+1], IMAGE[index1+2] = 0, 0, 0
            point_depart = point_depart[0], point_depart[1]+1
    elif direction == "haut":
        for i in range(longueur):
            index1 = 3 * ((y - i) * TAILLE +x)
            index2 = index1 +3
            INDEX_CHIFFRE.append(index1)
            INDEX_CHIFFRE.append(index2)
            IMAGE[index1], IMAGE[index1+1], IMAGE[index1+2] = 0, 0, 0
            IMAGE[index2], IMAGE[index2+1], IMAGE[index2+2] = 0, 0, 0
            point_depart = point_depart[0], point_depart[1]-1
    return point_depart
def trait_horizontal(point_depart, longueur, direction):
    """Dessine deux traits horizontal noir(un sur l'autre)."""
    x, y = int(point_depart[0]), int(point_depart[1])
    if direction == "droite":
        for i in range(longueur):
            index1 = 3 * (y * TAILLE + x + i)
            index2 = index1 - 3 * TAILLE
            INDEX_CHIFFRE.append(index1)
            INDEX_CHIFFRE.append(index2)
            IMAGE[index1], IMAGE[index1+1], IMAGE[index1+2] = 0, 0, 0
            IMAGE[index2], IMAGE[index2+1], IMAGE[index2+2] = 0, 0, 0
            point_depart = point_depart[0]+1, point_depart[1]
    elif direction == "gauche":
        for i in range(longueur):
            index1 = 3 * (y * TAILLE + x - i)
            index2 = index1 + 3*TAILLE
            INDEX_CHIFFRE.append(index1)
            INDEX_CHIFFRE.append(index2)
            IMAGE[index1], IMAGE[index1+1], IMAGE[index1+2] = 0, 0, 0
            IMAGE[index2], IMAGE[index2+1], IMAGE[index2+2] = 0, 0, 0
            point_depart = point_depart[0]-1, point_depart[1]
    return point_depart
def dessiner_chiffre(chiffre, point_depart, image):
    """Trace un chiffre au milieu de l'image"""
    longueur = int((5/100)*TAILLE)
    largeur = int(((1/5)*TAILLE)/(2*PRECISION+1))
    if chiffre == 0:
        point_depart = trait_horizontal(point_depart, largeur, "droite")
        point_depart = trait_vertical(point_depart, longueur, "bas")
        point_depart = trait_vertical(point_depart, longueur, "bas")
        point_depart = trait_horizontal(point_depart, largeur, "gauche")
        point_depart = trait_vertical(point_depart, longueur, "haut")
        point_depart = trait_vertical(point_depart, longueur, "haut")
    if chiffre == 1:
        point_depart = trait_vertical(point_depart, longueur, "bas")
        point_depart = trait_vertical(point_depart, longueur, "bas")
        index = 3 * (int(point_depart[1]) * TAILLE + int(point_depart[0]))
        image[index], image[index+1], image[index+2] = 0, 0, 0
    if chiffre == 2:
        point_depart = trait_horizontal(point_depart, largeur, "droite")
        point_depart = trait_vertical(point_depart, longueur, "bas")
        point_depart = trait_horizontal(point_depart, largeur, "gauche")
        point_depart = trait_vertical(point_depart, longueur, "bas")
        point_depart = trait_horizontal(point_depart, largeur, "droite")
    if chiffre == 3:
        point_depart = trait_horizontal(point_depart, largeur, "droite")
        point_depart = trait_vertical(point_depart, longueur, "bas")
        point_depart_2 = trait_horizontal(point_depart, largeur, "gauche")
        point_depart = trait_vertical(point_depart, longueur, "bas")
        point_depart = trait_horizontal(point_depart, largeur, "gauche")
    if chiffre == 4:
        point_depart = trait_vertical(point_depart, longueur, "bas")
        point_depart = trait_horizontal(point_depart, largeur, "droite")
        point_depart_2 = trait_vertical(point_depart, longueur, "bas")
        point_depart = trait_vertical(point_depart, longueur, "haut")
    if chiffre == 5:
        point_depart_2 = trait_horizontal(point_depart, largeur, "droite")
        point_depart = trait_vertical(point_depart, longueur, "bas")
        point_depart = trait_horizontal(point_depart, largeur, "droite")
        point_depart = trait_vertical(point_depart, longueur, "bas")
        point_depart = trait_horizontal(point_depart, largeur, "gauche")
    if chiffre == 6:
        point_depart_2 = trait_horizontal(point_depart, largeur, "droite")
        point_depart = trait_vertical(point_depart, longueur, "bas")
        point_depart = trait_horizontal(point_depart, largeur, "droite")
        point_depart = trait_vertical(point_depart, longueur, "bas")
        point_depart = trait_horizontal(point_depart, largeur, "gauche")
        point_depart = trait_vertical(point_depart, longueur, "haut")
    if chiffre == 7:
        point_depart = trait_horizontal(point_depart, largeur, "droite")
        point_depart = trait_vertical(point_depart, longueur, "bas")
        point_depart = trait_vertical(point_depart, longueur, "bas")
    if chiffre == 8:
        point_depart = trait_horizontal(point_depart, largeur, "droite")
        point_depart = trait_vertical(point_depart, longueur, "bas")
        point_depart = trait_horizontal(point_depart, largeur, "gauche")
        point_depart_2 = trait_vertical(point_depart, longueur, "haut")
        point_depart = trait_vertical(point_depart, longueur, "bas")
        point_depart = trait_horizontal(point_depart, largeur, "droite")
        point_depart = trait_vertical(point_depart, longueur, "haut")
    if chiffre == 9:
        point_depart = trait_horizontal(point_depart, largeur, "droite")
        point_depart = trait_vertical(point_depart, longueur, "bas")
        point_depart_2 = trait_horizontal(point_depart, largeur, "gauche")
        point_depart = trait_vertical(point_depart, longueur, "bas")
        point_depart_2 = trait_vertical(point_depart_2, longueur, "haut")
        point_depart = trait_horizontal(point_depart, largeur, "gauche")
def generate_ppm_file(ordre):
    """Cree une image ppm contenant l'approximation de pi"""
    # Adaper les points a la taille de l'image et les dessiner en rouge s'il
    # sont dans le cercle_unite,en bleu sinon
    global POINTS_CERCLE
    global INDEX_CHIFFRE
    INDEX_CHIFFRE = []
    for point in sim.generateur_points(nbr_point):
        point_adapte = sim.point((point[0]+1)*(TAILLE/2), (point[1]-1)*(TAILLE/2))
        x = int(point_adapte[0])
        y = int(point_adapte[1])
        index = 3 * (y * TAILLE +x)
        if sim.interieur_cercle(CERCLE_UNITE, point):
            POINTS_CERCLE += 1
            IMAGE[index] = 0
            IMAGE[index+1] = 0
            IMAGE[index+2] = 255
        else:
            IMAGE[index] = 255
            IMAGE[index+1] = 0
            IMAGE[index+2] = 127
    # Il faut maintenant dessiner l'approx de pi
    pi_approx = round(4*POINTS_CERCLE/((ordre+1)*nbr_point), PRECISION)
    liste_chiffre = list(str(pi_approx))
    apres_virgule = ''
    for i in range(2, len(liste_chiffre)):
        apres_virgule += liste_chiffre[i]
    largeur = int(((1/5)*TAILLE)/(2*PRECISION+1))
    longueur = int(0.05*TAILLE)
    #Dessiner le nombre 3
    point_depart = (0.4*TAILLE, 0.45*TAILLE)
    dessiner_chiffre(int(liste_chiffre[0]), point_depart, IMAGE)
    # Dessiner le point " . "
    point_depart = int(0.4*TAILLE+2*largeur), int(0.55*TAILLE)+1
    for i in range(int(longueur/7)):
        trait_vertical(point_depart, int(longueur/5), "haut")
        point_depart = point_depart[0]+1, point_depart[1]
    # Dessiner les chiffres apres la virgule
    for i in range(min(len(liste_chiffre)-2, PRECISION)):
        point_depart = (0.4*TAILLE+3*largeur+2*i*largeur, 0.45*TAILLE)
        dessiner_chiffre(int(liste_chiffre[2+i]), point_depart, IMAGE)
    # Creation de l'image ppm
    with open(f'img{ordre}_{int(pi_approx)}-{apres_virgule}.ppm', 'wb') as f_0:
        f_0.write(bytearray(PPM_HEADER, 'ascii'))
        IMAGE.tofile(f_0)
    for index in INDEX_CHIFFRE:
        IMAGE[index], IMAGE[index+1], IMAGE[index+2] = 192, 192, 192
def grid2gif(image_str, output_gif):
    """Regroupe des images en un fichier gif"""
    str1 = 'convert -delay 100 -loop 1 ' + image_str  + ' ' + output_gif
    subprocess.call(str1, shell=True)
def main():
    """Fonction principale du programme"""
    for i in range(10):
        generate_ppm_file(i)
    grid2gif("img*.ppm", "project.gif")
if __name__ == "__main__":
    main()
    print("--- %s seconds ---" % (time.time() - START_TIME))
