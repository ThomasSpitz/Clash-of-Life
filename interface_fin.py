import sys
import jeu
import interface_du_menu
import pygame


def retour():
    interface_du_menu.main_menu()
class TextInput:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 0, 0)  # Couleur initiale (noir)
        self.text = ''
        self.active = False

    def handle_text_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.color = (0, 0, 0)  # Le champ est actif
                print("Champ actif")
            else:
                self.active = False
                self.color = (169, 169, 169)  # Couleur grise quand inactif
                print("Champ inactif")

        if event.type == pygame.KEYDOWN:
            if self.active:
                print(f"Clé appuyée: {event.key}")
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_RETURN:
                    print(f"Valeur saisie avant retour: {self.text}")
                    return self.text  # Retourne le texte saisi
                elif event.unicode.isprintable():
                    self.text += event.unicode
                print(f"Texte actuel: {self.text}")
        return None


    def draw_text(self, screen,font):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        text_surface = font.render(self.text, True, (0, 0, 0))  # Texte noir
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))  # Affichage du texte


def Menu_fin():
    text_input = TextInput(400, 100, 200, 40)
        # Initialisation de Pygame
    pygame.init()
    pygame.mixer.init()
    # Définir les dimensions de la fenêtre
    H = 1600
    L = 800
    def draw(surface):
        interface_du_menu.draw(surface)
    # Définir les polices
    font = pygame.font.SysFont("Arial", 40)
    button_font = pygame.font.SysFont("Arial", 30)
    screen = pygame.display.set_mode((H, L))
    pygame.display.set_caption("FIN")
    running =True
    while running:
        screen.fill(interface_du_menu.BLACK)
        title_text = font.render("C'est fini", True, interface_du_menu.RED)
        screen.blit(title_text, (H // 2 - title_text.get_width() // 2, 50))
        entered_text='1400'


        rejouer= interface_du_menu.Button("REJOUER",450,300,100,30,interface_du_menu.Violet,lambda:interface_du_menu.start_game(entered_text))
        retour_menu=interface_du_menu.Button("MENU",450,225,100,30,interface_du_menu.RED,retour)
        quitter=interface_du_menu.Button("QUITTER",450,350,100,30,interface_du_menu.RED,interface_du_menu.quit_game)



        retour_menu.draw(screen,30)
        rejouer.draw(screen,30)
        quitter.draw(screen,30)
        text_input.draw_text(screen,font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()  # On arrête Pygame
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rejouer.is_hovered():
                    rejouer.click()                    
                elif quitter.is_hovered():
                    quitter.click()
                elif retour_menu.is_hovered():
                    retour_menu.click()
            result = text_input.handle_text_event(event)
            if result:
                entered_text = result     
        pygame.display.update()


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    Menu_fin()
