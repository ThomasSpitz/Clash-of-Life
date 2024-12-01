import pygame
from pygame.locals import *
from seed import *

def barre_vie(background,longueur,largeur,pourcentage,joueur):
    ##Creation de la barre de vie
    if joueur == 1:
        pygame.draw.rect(background, 'black', (0, 0, longueur/2, longueur*70/1800))
        pygame.draw.rect(background, (0,0,255), (longueur/90, longueur/90, (longueur/2-longueur/60)*pourcentage/100, longueur/60))
    elif joueur == 2:
        pygame.draw.rect(background, 'black', (longueur/2, 0, longueur/2, longueur*70/1800))
        pygame.draw.rect(background, (255,0,0), (longueur/2+10 +(1-pourcentage/100)*(longueur/2-longueur/60), longueur/90, (longueur/2-30)*pourcentage/100, longueur/60))

def barre_mana(background,longueur,largeur,pourcentage,joueur):
    ##Creation de la barre de mana

    if joueur == 1:
        pygame.draw.rect(background, 'black', (0, largeur - longueur*70/1800, longueur/2, longueur*70/1800))
        pygame.draw.rect(background, 'purple', (longueur/90 , largeur - largeur/18, (longueur/2-30)*pourcentage/100, longueur/60))
    elif joueur == 2:
        pygame.draw.rect(background, 'black', (longueur/2, largeur - longueur*70/1800, longueur/2, longueur*70/1800))
        pygame.draw.rect(background, 'purple', (longueur/2+longueur/180 + (1-pourcentage/100)*(longueur/2-longueur/60), largeur - largeur/18, (longueur/2-longueur/60)*pourcentage/100, longueur/60))
    for i in range(10):
        pygame.draw.rect(background, 'black', (longueur/90 + i*(longueur/2-longueur/60)/10, largeur - largeur/18, 1, longueur/60))
        pygame.draw.rect(background, 'black', (longueur/2+longueur/180 + i*(longueur/2-longueur/60)/10, largeur - largeur/18, 1, longueur/60))

def creer_interface(longueur,largeur):

    pygame.init()
    screen = pygame.display.set_mode((longueur,largeur))
    pygame.display.set_caption('Clash of life')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill('white')


    ##Creation des boutons sur les côtés
    pygame.draw.rect(background, 'black', (0, 0, longueur/12 + longueur/90, largeur))
    pygame.draw.rect(background, 'black', (longueur-longueur/12 - longueur/90, 0, longueur/12+longueur/90+10, largeur))

    for i in range(5):
        pygame.draw.rect(background, 'white', (longueur/90,i*longueur/12 + longueur/22.5, longueur/12 - longueur/90, longueur/12 - longueur/90))
        pygame.draw.rect(background, 'white', (longueur - longueur/12 ,i*longueur/12 + longueur/22.5, longueur/12 - longueur/90, longueur/12 - longueur/90))

    barre_vie(background,longueur,largeur,0,1)
    barre_vie(background,longueur,largeur,0,2)
    barre_mana(background,longueur,largeur,0,1)
    barre_mana(background,longueur,largeur,0,2)


    screen.blit(background, (0, 0))
    pygame.display.flip()
    for i in range(1000):
        barre_vie(background,longueur,largeur,i/10,1)
        barre_vie(background,longueur,largeur,i/10,2)
        barre_mana(background,longueur,largeur,i*30/1000,1)
        barre_mana(background,longueur,largeur,i*30/1000,2)

        screen.blit(background, (0, 0))
        pygame.display.flip()
    return screen,background
    
def afficher(universe,screen,background,x,y,ratio):
    for i in range(len(universe)):
        for j in range(len(universe[0])):
            if universe[i][j]==1:
                pygame.draw.rect(background,(0,0,255),Rect(x+j*ratio,y+i*ratio,ratio,ratio))
            elif universe[i][j]==2:
                pygame.draw.rect(background,(255,0,0),Rect(x+j*ratio,y+i*ratio,ratio,ratio))
            else :
                pygame.draw.rect(background,"white",Rect(x+j*ratio,y+i*ratio,ratio,ratio))
    screen.blit(background, (0, 0))
    pygame.display.flip()
        
def afficher_carte(background,screen,seed,joueur,numero,longueur,largeur): 
    if joueur == 1:
        ratio = (longueur/12 - longueur/90) / (max(len(seeds_blue[seed]),len(seeds_blue[seed][0])) + 2)
        for i in range(len(seeds_blue[seed])):
            for j in range(len(seeds_blue[seed][0])):
                if seeds_blue[seed][i][j] == 1:
                    pygame.draw.rect(background,(0,0,255),Rect(longueur/90 + (j+1)*ratio,numero*longueur/12 + longueur/22.5 + (i+1)*ratio,ratio,ratio))
    elif joueur == 2:
        ratio = (longueur/12 - longueur/90) / (max(len(seeds_red[seed]),len(seeds_red[seed][0])) + 2)
        for i in range(len(seeds_red[seed])):
            for j in range(len(seeds_red[seed][0])):
                if seeds_red[seed][i][j] == 2:
                    pygame.draw.rect(background,(255,0,0),Rect(longueur - longueur/12 + (j+1)*ratio,numero*longueur/12 + longueur/22.5 + (i+1)*ratio,ratio,ratio))
   
   
def draw_fictif(seed, x_start, y_start, ratio, background, longueur, universe):
    """Function to show in hindsight the seed for each player

    Args:
        seed (_list_): _list of the chosen seeds_
        x_start (_integer_): _x placement_
        y_start (_integer_): _y placement_
        ratio (_integer_): _ratio_
        background (_Surface_)
        longueur (_float_)
    """
    if seed == 0:
        pygame.draw.rect(background, 'black', (longueur/12 + longueur/90+y_start*ratio,longueur*70/1800+x_start*ratio,ratio,ratio))
    else:
        l=len(seed)
        L=len(seed[0])
        #assert len(seed)+x_start<= len(univers) and  len(seed)+y_start<= len(univers)
        for i in range(l):
            for j in range (L):
                if seed[i][j]== 1 or seed[i][j]== 2:
                    pygame.draw.rect(background, 'black', (longueur/12 + longueur/90+(((y_start+(j-L//2))%len(universe[0])))*ratio,longueur*70/1800+(((x_start+(i-l//2)))%len(universe))*ratio,ratio,ratio))