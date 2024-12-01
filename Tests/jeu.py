import pygame
import interface_pygame
import game_of_life
from seed import (
    seeds_blue,
    seeds_red,prix)
import interface_fin

def main(longueur,largeur,deck_blue,deck_red):
    """Fonction configurant et réalisant le jeu

    Args:
        longueur (_integer_): _resolution horizontale_
        largeur (_integer_): _resolution verticale_
        deck_blue (_list_): _list with the available seeds for blue_
        deck_red (_list_): _list with the available seeds for red_
    """
    #Variables:
    x_size = 76
    y_size = 146
    step = 4
    x_start_blue=step*2
    y_start_blue=int(3*y_size/8)
    x_start_red=step*2
    y_start_red=int(5*y_size/8)
    seed_blue=0
    seed_red=0
    mana_blue = 30
    mana_red = 30
    size_tape=longueur/90
    size_display_seed=longueur/12
    ratio = (longueur-2*size_display_seed-2*size_tape)/y_size
    
    #Initialisation display:
    background,screen=interface_pygame.creer_interface(longueur,largeur)
    for i in range(5):
        interface_pygame.afficher_carte(background,screen,deck_blue[i],1,i,longueur,largeur)
        interface_pygame.afficher_carte(background,screen,deck_red[i],2,i,longueur,largeur)
    pygame.display.flip()
    universe=[[0 for i in range(y_size)] for j in range(x_size)]
    #clock = pygame.time.Clock()
    
    #Move configuration for each player:
    while 1 :
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    y_start_red=int(y_size/2 + (y_start_red - y_size/2 - step) % (y_size/4))
                if event.key == pygame.K_RIGHT:
                    y_start_red = int(y_size/2 + (y_start_red - y_size/2 + step) % (y_size/4))
                if event.key == pygame.K_UP:
                    x_start_red = int((x_start_red- step )% x_size)
                if event.key == pygame.K_DOWN:
                    x_start_red= int((x_start_red +step) % x_size)
                if event.key == pygame.K_q:
                    y_start_blue=int(y_size/4 + (y_start_blue -y_size/4 -step)% (y_size/4) )
                if event.key == pygame.K_d:
                    y_start_blue = int(y_size/4 +(y_start_blue -y_size/4 +step)% (y_size/4) )
                if event.key == pygame.K_z:
                    x_start_blue = int((x_start_blue -step )%x_size)
                if event.key == pygame.K_s:
                    x_start_blue= int((x_start_blue +step) % x_size)
                if event.key == pygame.K_1:
                    if seed_blue==seeds_blue[deck_blue[0]]:
                        if mana_blue < prix[deck_blue[0]]:
                            break 
                        universe=game_of_life.add_seed_to_universe(seeds_blue[deck_blue[0]],universe,x_start_blue,y_start_blue)
                        mana_blue-=prix[deck_blue[0]]
                    else:
                        seed_blue=seeds_blue[deck_blue[0]]

                if event.key == pygame.K_2:
                    if seed_blue==seeds_blue[deck_blue[1]]:   
                                      
                        if mana_blue < prix[deck_blue[1]]:
                            break
                        universe=game_of_life.add_seed_to_universe(seeds_blue[deck_blue[1]],universe,x_start_blue,y_start_blue)
                        mana_blue-=prix[deck_blue[1]]
                    else:
                        seed_blue=seeds_blue[deck_blue[1]]
                if event.key == pygame.K_3: 
                    if seed_blue==seeds_blue[deck_blue[2]]:
                        
                        if mana_blue < prix[deck_blue[2]]:
                            break
                        universe=game_of_life.add_seed_to_universe(seeds_blue[deck_blue[2]],universe,x_start_blue,y_start_blue)
                        mana_blue-=prix[deck_blue[2]]
                    else:
                        seed_blue=seeds_blue[deck_blue[2]] 

                if event.key == pygame.K_4:
                    if seed_blue==seeds_blue[deck_blue[3]]:
                      
                        if mana_blue< prix[deck_blue[3]]:
                            break
                        universe=game_of_life.add_seed_to_universe(seeds_blue[deck_blue[3]],universe,x_start_blue,y_start_blue)
                        mana_blue-=prix[deck_blue[3]]
                    else:
                        seed_blue=seeds_blue[deck_blue[3]]
                if event.key == pygame.K_5: 
                    if seed_blue==seeds_blue[deck_blue[4]]:
                        if mana_blue < prix[deck_blue[4]]:
                            break
                        universe=game_of_life.add_seed_to_universe(seeds_blue[deck_blue[4]],universe,x_start_blue,y_start_blue)
                        mana_blue-=prix[deck_blue[4]]
                    else:
                        seed_blue=seeds_blue[deck_blue[4]]
                if event.key == pygame.K_6: 
                    if seed_red==seeds_red[deck_red[0]] :
                        if mana_red < prix[deck_red[0]]:
                            break
                        universe=game_of_life.add_seed_to_universe(seeds_red[deck_red[0]],universe,x_start_red,y_start_red)
                        mana_red-=prix[deck_red[0]]
                    else:
                        seed_red=seeds_red[deck_red[0]]
                if event.key == pygame.K_7:  
                    if seed_red==seeds_red[deck_red[1]]:
                        if mana_red < prix[deck_red[1]]:
                            break
                        universe=game_of_life.add_seed_to_universe(seeds_red[deck_red[1]],universe,x_start_red,y_start_red)
                        mana_red-=prix[deck_red[1]]
                    else:
                        seed_red=seeds_red[deck_red[1]]
                if event.key == pygame.K_8:
                    if seed_red==seeds_red[deck_red[2]]:
                        if mana_red < prix[deck_red[2]]:
                            break
                        universe=game_of_life.add_seed_to_universe(seeds_red[deck_red[2]],universe,x_start_red,y_start_red)
                        mana_red-=prix[deck_red[2]]
                    else:
                        seed_red=seeds_red[deck_red[2]]
                if event.key == pygame.K_9: 
                    if seed_red==seeds_red[deck_red[3]]:
                        if mana_red < prix[deck_red[3]]:
                            break
                        universe=game_of_life.add_seed_to_universe(seeds_red[deck_red[3]],universe,x_start_red,y_start_red)
                        mana_red-=prix[deck_red[3]]
                    else:
                        seed_red=seeds_red[deck_red[3]]
                if event.key == pygame.K_0:
                    if seed_red==seeds_red[deck_red[4]] :
                        if mana_red < prix[deck_red[4]]:
                            break
                        universe=game_of_life.add_seed_to_universe(seeds_red[deck_red[4]],universe,x_start_red,y_start_red)
                        mana_red-=prix[deck_red[4]]
                    else:
                        seed_red=seeds_red[deck_red[4]]



        
        interface_pygame.afficher(universe,screen,background,size_tape + size_display_seed,longueur*70/1800,ratio)
        universe = game_of_life.refresh(universe)
        
        #Show in hindsight the seed for each player:
        interface_pygame.draw_fictif(seed_blue, x_start_blue, y_start_blue, ratio, background, longueur, universe)
        interface_pygame.draw_fictif(seed_red, x_start_red, y_start_red, ratio, background, longueur, universe)
        
        #Mana Management:
        if game_of_life.pdv_blue <= 0 or game_of_life.pdv_red <= 0:
            pygame.quit()
            interface_fin.Menu_fin()
        interface_pygame.barre_vie(background,longueur,largeur,game_of_life.pdv_blue,1)
        interface_pygame.barre_vie(background,longueur,largeur,game_of_life.pdv_red,2)
        interface_pygame.barre_mana(background,longueur,largeur,mana_blue,1)
        interface_pygame.barre_mana(background,longueur,largeur,mana_red,2)
        mana_blue = min(mana_blue+0.1,100)
        mana_red = min(mana_red+0.1,100)
        screen.blit(background, (0, 0))
        pygame.display.flip()

#main(1400, 700, ['P14', 'P14', 'P14', 'P14', 'P14'], ['P14', 'P14', 'P14', 'P14', 'P14'])
