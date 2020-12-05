#!/usr/bin/python
# -*-coding:Utf-8 -*

import pygame
from pygame.locals import *
pygame.init()

fenetre = pygame.display.set_mode((1025, 700))
pygame.display.set_caption("Grosse Krabbelei")



piece_1_X = 710
piece_1_Y = 410
piece_1_position = 0
piece_1_rotate = 1
piece_2_X = 855
piece_2_Y = 410
piece_2_position = 0
piece_2_rotate = 1
piece_3_X = 710
piece_3_Y = 555
piece_3_position = 0
piece_3_rotate = 1
piece_4_X = 855
piece_4_Y = 555
piece_4_position = 0
piece_4_rotate = 1

level = 1

"""pièce 1
			001
			111
			110			"""
piece_1 = pygame.image.load("Grosse_Krabbelei_Image/piece_1.png").convert_alpha()
piece_1 = pygame.transform.scale(piece_1, (135,135))

"""pièce 2
			111
			010
			111			"""
piece_2 = pygame.image.load("Grosse_Krabbelei_Image/piece_2.png").convert_alpha()
piece_2 = pygame.transform.scale(piece_2, (135,135))

"""pièce 3
			101
			101
			111			"""
piece_3 = pygame.image.load("Grosse_Krabbelei_Image/piece_3.png").convert_alpha()
piece_3 = pygame.transform.scale(piece_3, (135,135))

"""pièce 4
			110
			111
			101			"""
piece_4 = pygame.image.load("Grosse_Krabbelei_Image/piece_4.png").convert_alpha()
piece_4 = pygame.transform.scale(piece_4, (135,135))


fleche_gauche = pygame.image.load("Grosse_Krabbelei_Image/fleche_gauche.png").convert_alpha()
fleche_bas = pygame.Rect((720, 190), (20, 20))
fleche_droite = pygame.image.load("Grosse_Krabbelei_Image/fleche_droite.png").convert_alpha()
fleche_haut = pygame.Rect((960, 190), (20, 20))

case_1 = pygame.Rect((35, 35), (300, 300))
case_2 = pygame.Rect((35, 365), (300, 300))
case_3 = pygame.Rect((365, 35), (300, 300))
case_4 = pygame.Rect((365, 365), (300, 300))

#niveau, rouge, violet, orange, rose, blanc
image_level = ["liste des niveaux",
["Grosse_Krabbelei_Image/1.png","Grosse_Krabbelei_Image/5x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png"],
["Grosse_Krabbelei_Image/2.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/5x.png","Grosse_Krabbelei_Image/0x.png"],
["Grosse_Krabbelei_Image/3.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/4x.png"],
["Grosse_Krabbelei_Image/4.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/4x.png","Grosse_Krabbelei_Image/3x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png"],
["Grosse_Krabbelei_Image/5.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/6x.png","Grosse_Krabbelei_Image/1x.png"],
["Grosse_Krabbelei_Image/6.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/3x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/3x.png"],
["Grosse_Krabbelei_Image/7.png","Grosse_Krabbelei_Image/3x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/4x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png"],
["Grosse_Krabbelei_Image/8.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/3x.png"],
["Grosse_Krabbelei_Image/9.png","Grosse_Krabbelei_Image/3x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/4x.png"],
["Grosse_Krabbelei_Image/10.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/3x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/0x.png"],
["Grosse_Krabbelei_Image/11.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/1x.png"],
["Grosse_Krabbelei_Image/12.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/3x.png","Grosse_Krabbelei_Image/4x.png"],
["Grosse_Krabbelei_Image/13.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/3x.png","Grosse_Krabbelei_Image/0x.png"],
["Grosse_Krabbelei_Image/14.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/2x.png"],
["Grosse_Krabbelei_Image/15.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/5x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png"],
["Grosse_Krabbelei_Image/16.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png"],
["Grosse_Krabbelei_Image/17.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/3x.png"],
["Grosse_Krabbelei_Image/18.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png"],
["Grosse_Krabbelei_Image/19.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/5x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png"],
["Grosse_Krabbelei_Image/20.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/1x.png"],
["Grosse_Krabbelei_Image/21.png","Grosse_Krabbelei_Image/3x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/3x.png"],
["Grosse_Krabbelei_Image/22.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png"],
["Grosse_Krabbelei_Image/23.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/4x.png"],
["Grosse_Krabbelei_Image/24.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png"],
["Grosse_Krabbelei_Image/25.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/4x.png","Grosse_Krabbelei_Image/1x.png"],
["Grosse_Krabbelei_Image/26.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/4x.png"],
["Grosse_Krabbelei_Image/27.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/3x.png","Grosse_Krabbelei_Image/3x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png"],
["Grosse_Krabbelei_Image/28.png","Grosse_Krabbelei_Image/4x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/3x.png"],
["Grosse_Krabbelei_Image/29.png","Grosse_Krabbelei_Image/3x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/3x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/2x.png"],
["Grosse_Krabbelei_Image/30.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/3x.png"],
["Grosse_Krabbelei_Image/31.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png"],
["Grosse_Krabbelei_Image/32.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/3x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/3x.png"],
["Grosse_Krabbelei_Image/33.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png"],
["Grosse_Krabbelei_Image/34.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/4x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/2x.png"],
["Grosse_Krabbelei_Image/35.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/3x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/3x.png"],
["Grosse_Krabbelei_Image/36.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png"],
["Grosse_Krabbelei_Image/37.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/3x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/1x.png"],
["Grosse_Krabbelei_Image/38.png","Grosse_Krabbelei_Image/4x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png"],
["Grosse_Krabbelei_Image/39.png","Grosse_Krabbelei_Image/3x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/0x.png"],
["Grosse_Krabbelei_Image/40.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/3x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/1x.png"],
["Grosse_Krabbelei_Image/41.png","Grosse_Krabbelei_Image/4x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/2x.png"],
["Grosse_Krabbelei_Image/42.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/4x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png"],
["Grosse_Krabbelei_Image/43.png","Grosse_Krabbelei_Image/4x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/0x.png"],
["Grosse_Krabbelei_Image/44.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/3x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/3x.png"],
["Grosse_Krabbelei_Image/45.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/2x.png"],
["Grosse_Krabbelei_Image/46.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/4x.png"],
["Grosse_Krabbelei_Image/47.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/0x.png","Grosse_Krabbelei_Image/3x.png"],
["Grosse_Krabbelei_Image/48.png","Grosse_Krabbelei_Image/3x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/1x.png","Grosse_Krabbelei_Image/2x.png","Grosse_Krabbelei_Image/1x.png"]
]


def affichage():

	#plateau
	pygame.draw.rect(fenetre, (88,41,0), (0, 0, 1025, 700))

	#4case
	pygame.draw.rect(fenetre, (205,133,63), (35, 35, 300, 300))
	pygame.draw.rect(fenetre, (205,133,63), (35, 365, 300, 300))
	pygame.draw.rect(fenetre, (205,133,63), (365, 35, 300, 300))
	pygame.draw.rect(fenetre, (205,133,63), (365, 365, 300, 300))

	#couleur rouge
	pygame.draw.rect(fenetre, (255,0,0), (45, 45, 80, 80))
	pygame.draw.rect(fenetre, (255,0,0), (245, 245, 80, 80))
	pygame.draw.rect(fenetre, (255,0,0), (575, 145, 80, 80))
	pygame.draw.rect(fenetre, (255,0,0), (145, 375, 80, 80))
	pygame.draw.rect(fenetre, (255,0,0), (475, 575, 80, 80))

	#couleur violet
	pygame.draw.rect(fenetre, (129,20,83), (45, 145, 80, 80))
	pygame.draw.rect(fenetre, (129,20,83), (245, 145, 80, 80))
	pygame.draw.rect(fenetre, (129,20,83), (475, 145, 80, 80))
	pygame.draw.rect(fenetre, (129,20,83), (245, 375, 80, 80))
	pygame.draw.rect(fenetre, (129,20,83), (575, 575, 80, 80))

	#couleur orange
	pygame.draw.rect(fenetre, (255,140,0), (45, 245, 80, 80))
	pygame.draw.rect(fenetre, (255,140,0), (475, 245, 80, 80))
	pygame.draw.rect(fenetre, (255,140,0), (45, 375, 80, 80))
	pygame.draw.rect(fenetre, (255,140,0), (245, 575, 80, 80))
	pygame.draw.rect(fenetre, (255,140,0), (475, 475, 80, 80))

	#couleur rose
	pygame.draw.rect(fenetre, (255,105,180), (145, 145, 80, 80))
	pygame.draw.rect(fenetre, (255,105,180), (375, 45, 80, 80))
	pygame.draw.rect(fenetre, (255,105,180), (575, 245, 80, 80))
	pygame.draw.rect(fenetre, (255,105,180), (45, 475, 80, 80))
	pygame.draw.rect(fenetre, (255,105,180), (245, 475, 80, 80))
	pygame.draw.rect(fenetre, (255,105,180), (375, 575, 80, 80))

	#couleur blanc
	pygame.draw.rect(fenetre, (245,245,220), (245, 45, 80, 80))
	pygame.draw.rect(fenetre, (245,245,220), (145, 245, 80, 80))
	pygame.draw.rect(fenetre, (245,245,220), (575, 45, 80, 80))
	pygame.draw.rect(fenetre, (245,245,220), (375, 245, 80, 80))
	pygame.draw.rect(fenetre, (245,245,220), (45, 575, 80, 80))
	pygame.draw.rect(fenetre, (245,245,220), (575, 475, 80, 80))


	#affichage piece
	fenetre.blit(piece_1, (piece_1_X, piece_1_Y))
	fenetre.blit(piece_2, (piece_2_X, piece_2_Y))
	fenetre.blit(piece_3, (piece_3_X, piece_3_Y))
	fenetre.blit(piece_4, (piece_4_X, piece_4_Y))

	#case du niveau
	pygame.draw.rect(fenetre, (205,133,63), (710, 10, 280, 380))

	#fleche
	fenetre.blit(fleche_gauche, (720, 190))
	fenetre.blit(fleche_droite, (960, 190))

	#niveau
	niveau = pygame.image.load(image_level[level][0]).convert_alpha()
	fenetre.blit(niveau, (710, 10))

	#x fois
	x_fois = pygame.image.load("Grosse_Krabbelei_Image/x.png").convert_alpha()
	fenetre.blit(x_fois, (710, 125))
	fenetre.blit(x_fois, (710, 175))
	fenetre.blit(x_fois, (710, 225))
	fenetre.blit(x_fois, (710, 275))
	fenetre.blit(x_fois, (710, 325))

	#nombre fois
	nombre_fois = pygame.image.load(image_level[level][1]).convert_alpha()
	fenetre.blit(nombre_fois, (710, 125))
	nombre_fois = pygame.image.load(image_level[level][2]).convert_alpha()
	fenetre.blit(nombre_fois, (710, 175))
	nombre_fois = pygame.image.load(image_level[level][3]).convert_alpha()
	fenetre.blit(nombre_fois, (710, 225))
	nombre_fois = pygame.image.load(image_level[level][4]).convert_alpha()
	fenetre.blit(nombre_fois, (710, 275))
	nombre_fois = pygame.image.load(image_level[level][5]).convert_alpha()
	fenetre.blit(nombre_fois, (710, 325))

	#couleurs fois
	pygame.draw.rect(fenetre, (255,0,0), (855, 130, 37, 37))
	pygame.draw.rect(fenetre, (129,20,83), (855, 180, 37, 37))
	pygame.draw.rect(fenetre, (255,140,0), (855, 230, 37, 37))
	pygame.draw.rect(fenetre, (255,105,180), (855, 280, 37, 37))
	pygame.draw.rect(fenetre, (245,245,220), (855, 330, 37, 37))




affichage()
loop = 1

while loop:	

	for event in pygame.event.get():

		if event.type == QUIT:
			loop = 0



		if event.type == MOUSEBUTTONUP and event.button == 1:

			if fleche_bas.collidepoint(event.pos) and level > 1:
				level = level - 1

				piece_1_X = 710
				piece_1_Y = 410
				piece_1_position = 0
				piece_1 = pygame.image.load("Grosse_Krabbelei_Image/piece_1.png").convert_alpha()
				piece_1 = pygame.transform.scale(piece_1, (135,135))
				piece_1_rotate = 1
				piece_2_X = 855
				piece_2_Y = 410
				piece_2_position = 0
				piece_2 = pygame.image.load("Grosse_Krabbelei_Image/piece_2.png").convert_alpha()
				piece_2 = pygame.transform.scale(piece_2, (135,135))
				piece_2_rotate = 1
				piece_3_X = 710
				piece_3_Y = 555
				piece_3_position = 0
				piece_3 = pygame.image.load("Grosse_Krabbelei_Image/piece_3.png").convert_alpha()
				piece_3 = pygame.transform.scale(piece_3, (135,135))
				piece_3_rotate = 1
				piece_4_X = 855
				piece_4_Y = 555
				piece_4_position = 0
				piece_4 = pygame.image.load("Grosse_Krabbelei_Image/piece_4.png").convert_alpha()
				piece_4 = pygame.transform.scale(piece_4, (135,135))
				piece_4_rotate = 1

			if fleche_haut.collidepoint(event.pos) and level < 48:
				level = level + 1

				piece_1_X = 710
				piece_1_Y = 410
				piece_1_position = 0
				piece_1 = pygame.image.load("Grosse_Krabbelei_Image/piece_1.png").convert_alpha()
				piece_1 = pygame.transform.scale(piece_1, (135,135))
				piece_1_rotate = 1
				piece_2_X = 855
				piece_2_Y = 410
				piece_2_position = 0
				piece_2 = pygame.image.load("Grosse_Krabbelei_Image/piece_2.png").convert_alpha()
				piece_2 = pygame.transform.scale(piece_2, (135,135))
				piece_2_rotate = 1
				piece_3_X = 710
				piece_3_Y = 555
				piece_3_position = 0
				piece_3 = pygame.image.load("Grosse_Krabbelei_Image/piece_3.png").convert_alpha()
				piece_3 = pygame.transform.scale(piece_3, (135,135))
				piece_3_rotate = 1
				piece_4_X = 855
				piece_4_Y = 555
				piece_4_position = 0
				piece_4 = pygame.image.load("Grosse_Krabbelei_Image/piece_4.png").convert_alpha()
				piece_4 = pygame.transform.scale(piece_4, (135,135))
				piece_4_rotate = 1




			affichage()


		if event.type == MOUSEBUTTONDOWN and event.button == 1:

			if piece_1.get_rect(topleft=(piece_1_X,piece_1_Y)).collidepoint(event.pos):
				piece_1 = pygame.transform.scale(piece_1, (300,300))
				move = 1
				while move:
					for event in pygame.event.get():
						piece_1_X, piece_1_Y = pygame.mouse.get_pos()
						piece_1_X = piece_1_X - 150
						piece_1_Y = piece_1_Y - 150
						affichage()
						pygame.display.flip()
						if event.type == pygame.KEYDOWN and event.key == K_SPACE:
							if piece_1_rotate == 1:
								piece_1 = pygame.transform.rotate(piece_1, 90)
								piece_1_rotate = 2
							elif piece_1_rotate == 2:
								piece_1 = pygame.transform.rotate(piece_1, 90)
								piece_1_rotate = 3
							elif piece_1_rotate == 3:
								piece_1 = pygame.transform.rotate(piece_1, 90)
								piece_1_rotate = 4
							else:
								piece_1 = pygame.transform.rotate(piece_1, 90)
								piece_1_rotate = 1


						elif event.type == MOUSEBUTTONUP and event.button == 1:
							if case_1.collidepoint(event.pos):
								piece_1_X = case_1.x
								piece_1_Y = case_1.y
								piece_1_position = 1
							elif case_2.collidepoint(event.pos):
								piece_1_X = case_2.x
								piece_1_Y = case_2.y
								piece_1_position = 2
							elif case_3.collidepoint(event.pos):
								piece_1_X = case_3.x
								piece_1_Y = case_3.y
								piece_1_position = 3
							elif case_4.collidepoint(event.pos):
								piece_1_X = case_4.x
								piece_1_Y = case_4.y
								piece_1_position = 4
							else:
								piece_1_X = 710
								piece_1_Y = 410
								piece_1_position = 0
								piece_1 = pygame.image.load("Grosse_Krabbelei_Image/piece_1.png").convert_alpha()
								piece_1 = pygame.transform.scale(piece_1, (135,135))
								piece_1_rotate = 1

							affichage()
							move = 0


			if piece_2.get_rect(topleft=(piece_2_X,piece_2_Y)).collidepoint(event.pos):
				piece_2 = pygame.transform.scale(piece_2, (300,300))
				move = 1
				while move:
					for event in pygame.event.get():
						piece_2_X, piece_2_Y = pygame.mouse.get_pos()
						piece_2_X = piece_2_X - 150
						piece_2_Y = piece_2_Y - 150
						affichage()
						pygame.display.flip()
						if event.type == pygame.KEYDOWN and event.key == K_SPACE:
							if piece_2_rotate == 1:
								piece_2 = pygame.transform.rotate(piece_2, 90)
								piece_2_rotate = 2
							else:
								piece_2 = pygame.transform.rotate(piece_2, 90)
								piece_2_rotate = 1


						elif event.type == MOUSEBUTTONUP and event.button == 1:
							if case_1.collidepoint(event.pos):
								piece_2_X = case_1.x
								piece_2_Y = case_1.y
								piece_2_position = 1
							elif case_2.collidepoint(event.pos):
								piece_2_X = case_2.x
								piece_2_Y = case_2.y
								piece_2_position = 2
							elif case_3.collidepoint(event.pos):
								piece_2_X = case_3.x
								piece_2_Y = case_3.y
								piece_2_position = 3
							elif case_4.collidepoint(event.pos):
								piece_2_X = case_4.x
								piece_2_Y = case_4.y
								piece_2_position = 4
							else:
								piece_2_X = 855
								piece_2_Y = 410
								piece_2_position = 0
								piece_2 = pygame.image.load("Grosse_Krabbelei_Image/piece_2.png").convert_alpha()
								piece_2 = pygame.transform.scale(piece_2, (135,135))
								piece_2_rotate = 1

							affichage()
							move = 0


			if piece_3.get_rect(topleft=(piece_3_X,piece_3_Y)).collidepoint(event.pos):
				piece_3 = pygame.transform.scale(piece_3, (300,300))
				move = 1
				while move:
					for event in pygame.event.get():
						piece_3_X, piece_3_Y = pygame.mouse.get_pos()
						piece_3_X = piece_3_X - 150
						piece_3_Y = piece_3_Y - 150
						affichage()
						pygame.display.flip()
						if event.type == pygame.KEYDOWN and event.key == K_SPACE:
							if piece_3_rotate == 1:
								piece_3 = pygame.transform.rotate(piece_3, 90)
								piece_3_rotate = 2
							elif piece_3_rotate == 2:
								piece_3 = pygame.transform.rotate(piece_3, 90)
								piece_3_rotate = 3
							elif piece_3_rotate == 3:
								piece_3 = pygame.transform.rotate(piece_3, 90)
								piece_3_rotate = 4
							else:
								piece_3 = pygame.transform.rotate(piece_3, 90)
								piece_3_rotate = 1


						elif event.type == MOUSEBUTTONUP and event.button == 1:
							if case_1.collidepoint(event.pos):
								piece_3_X = case_1.x
								piece_3_Y = case_1.y
								piece_3_position = 1
							elif case_2.collidepoint(event.pos):
								piece_3_X = case_2.x
								piece_3_Y = case_2.y
								piece_3_position = 2
							elif case_3.collidepoint(event.pos):
								piece_3_X = case_3.x
								piece_3_Y = case_3.y
								piece_3_position = 3
							elif case_4.collidepoint(event.pos):
								piece_3_X = case_4.x
								piece_3_Y = case_4.y
								piece_3_position = 4
							else:
								piece_3_X = 710
								piece_3_Y = 555
								piece_3_position = 0
								piece_3 = pygame.image.load("Grosse_Krabbelei_Image/piece_3.png").convert_alpha()
								piece_3 = pygame.transform.scale(piece_3, (135,135))
								piece_3_rotate = 1

							affichage()
							move = 0


			if piece_4.get_rect(topleft=(piece_4_X,piece_4_Y)).collidepoint(event.pos):
				piece_4 = pygame.transform.scale(piece_4, (300,300))
				move = 1
				while move:
					for event in pygame.event.get():
						piece_4_X, piece_4_Y = pygame.mouse.get_pos()
						piece_4_X = piece_4_X - 150
						piece_4_Y = piece_4_Y - 150
						affichage()
						pygame.display.flip()
						if event.type == pygame.KEYDOWN and event.key == K_SPACE:
							if piece_4_rotate == 1:
								piece_4 = pygame.transform.rotate(piece_4, 90)
								piece_4_rotate = 2
							elif piece_4_rotate == 2:
								piece_4 = pygame.transform.rotate(piece_4, 90)
								piece_4_rotate = 3
							elif piece_4_rotate == 3:
								piece_4 = pygame.transform.rotate(piece_4, 90)
								piece_4_rotate = 4
							else:
								piece_4 = pygame.transform.rotate(piece_4, 90)
								piece_4_rotate = 1


						elif event.type == MOUSEBUTTONUP and event.button == 1:
							if case_1.collidepoint(event.pos):
								piece_4_X = case_1.x
								piece_4_Y = case_1.y
								piece_4_position = 1
							elif case_2.collidepoint(event.pos):
								piece_4_X = case_2.x
								piece_4_Y = case_2.y
								piece_4_position = 2
							elif case_3.collidepoint(event.pos):
								piece_4_X = case_3.x
								piece_4_Y = case_3.y
								piece_4_position = 3
							elif case_4.collidepoint(event.pos):
								piece_4_X = case_4.x
								piece_4_Y = case_4.y
								piece_4_position = 4
							else:
								piece_4_X = 855
								piece_4_Y = 555
								piece_4_position = 0
								piece_4 = pygame.image.load("Grosse_Krabbelei_Image/piece_4.png").convert_alpha()
								piece_4 = pygame.transform.scale(piece_4, (135,135))
								piece_4_rotate = 1

							affichage()
							move = 0





	pygame.display.flip()