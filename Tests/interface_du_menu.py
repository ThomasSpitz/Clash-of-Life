import jeu

import pygame
import sys

from tkinter import Tk, Button

# Initialisation de Pygame
pygame.init()
pygame.mixer.init()
# Définir les dimensions de la fenêtre
L = 1024
H = 768
screen = pygame.display.set_mode((L, H), pygame.RESIZABLE)
pygame.display.set_caption("GAME OF LIFE")

# Options pour les différentes tailles
options = {
    "Petit": (640, 480),
    "Moyen": (800, 600),
    "Grand": (1024, 768)
}


# Définir les couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (220, 20, 60)
BLUE = (0, 128, 255)
GRAY = (200, 200, 200)
Turquoise =(64, 224, 208)
Or = (255, 215, 0)
Violet =(238, 130, 238)
Indigo =(75, 0, 130)
Rouge_foncé= (139, 0, 0)
Beige= (245, 245, 220)
Marron = (139, 69, 19)
Rose = (255, 105, 180)
# Définir les polices
font = pygame.font.SysFont("Arial", 40)
button_font = pygame.font.SysFont("Arial", 30)
#La Musique
pygame.mixer.music.load('Audio\\musique_menu.mp3')
son1 = pygame.mixer.Sound('Audio\\sus.mp3')
# Jouer la musique
pygame.mixer.music.play(-1)

def draw_input_box(input_text):
    """Dessiner le champ de saisie de texte"""
    pygame.draw.rect(screen, BLUE, (600, 600, 300, 40), 2)  # Dessiner le cadre du champ de saisie
    text_surface = font.render(input_text, True, BLACK)
    screen.blit(text_surface, (605, 605))  # Afficher le texte dans le champ de saisie


# Dictionnaires pour les decks
d1 = []
d2 = []

ship = {
    "Wing" : "Wing",
    "MWSS" : "MWSS",
    "MWSSXMWSS" : "MWSSXMWSS",
    "BigA" : "BigA",
    "Big_Glider" : "Big Glider",
    "Brain" : "Brain",
    "Barge2" : "Barge2",
    "Turtle" : "Turtle",
    "Crab" : "Crab",
    "Dart" : "Dart",
    "Lobster" : "Lobster",
    "Hivenudger" : "Hivenudger",
    "Hammerhead" : "Hammerhead",
    "P3H" : "P3H",
    "Canada_Goose" : "Goose",
    "Queen_bee" : "Queen Bee",
    "P14" : "P14",
    "P36" : "P36",
    "Babbling_brook" : "Brook",
    "Pi_heptomino" : "Pi",
    "Simkin_glider" : "Simkin",
    "Gosper_Glider_Gun" : "Gosper"
        }

def ajoute(d, vaisseau):
    """Ajoute un vaisseau au deck et affiche le résultat"""
    if len(d) < 5 and vaisseau not in d:
        d.append(vaisseau)
    if len(d) == 5 and vaisseau not in d:
        for i in range(1,5):
            d[5-i] = d[4-i]
        d[0] = vaisseau
    print(d)

# Classe pour les boutons
class Button:
    def __init__(self, text, x, y, width, height, color, action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.base_color = self.clamp_color(color)  # Couleur de base
        self.hover_color = self.clamp_color((color[0] - 20, color[1] - 20, color[2] - 20))  # Plus sombre
        self.shadow_color = self.clamp_color((150, 150, 150))  # Ombre douce
        self.click_color = self.clamp_color((color[0] - 40, color[1] - 40, color[2] - 40))  # Couleur au clic
        self.color = self.base_color
        self.action = action
        self.clicked = False
        self.is_being_clicked = False
        self.radius = 10
        self.shadow_offset = 6

    @staticmethod
    def clamp_color(color):
        """S'assure que chaque composante de couleur est dans l'intervalle [0, 255]."""
        return tuple(max(0, min(255, c)) for c in color)

    def draw(self, surface, font_size):
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = self.is_hovered()
        font = pygame.font.Font(None, font_size)

        # Ombre du bouton
        shadow_rect = self.rect.move(self.shadow_offset, self.shadow_offset)
        pygame.draw.rect(surface, self.shadow_color, shadow_rect, border_radius=self.radius)

        # Couleur du bouton selon l'état
        if self.is_being_clicked:
            self.color = self.click_color
        elif is_hovered:
            self.color = self.hover_color
        else:
            self.color = self.base_color

        # Dessiner le bouton
        pygame.draw.rect(surface, self.color, self.rect, border_radius=self.radius)

        # Texte centré dans le bouton
        text_surface = font.render(self.text, True, BLACK)  # Crée la surface avec le texte
        surface.blit(
            text_surface,
            (
                self.rect.x + (self.rect.width - text_surface.get_width()) // 2,
                self.rect.y + (self.rect.height - text_surface.get_height()) // 2,
            ),
        )

    def is_hovered(self):
        """Vérifie si la souris survole le bouton."""
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def click(self):
        """Active l'action si le bouton est cliqué."""
        if self.is_hovered():
            if self.action:
                self.action()
            self.clicked = True

    def on_mouse_button_down(self):
        """Déclenche l'effet de clic."""
        if self.is_hovered():
            self.is_being_clicked = True

    def on_mouse_button_up(self):
        """Relâche l'effet de clic."""
        self.is_being_clicked = False
        if self.is_hovered():
            self.click()




def afficher_texte(x, y, texte, couleur, taille=36):
    font = pygame.font.Font(None, taille)
    text_surface = font.render(texte, True, couleur)
    screen.blit(text_surface, (x, y))
# Fonctions pour démarrer et quitter le jeu
def start_game(valeur):
    """Action pour démarrer le jeu"""
    
    print(valeur)
    SCREEN_WIDTH=int(valeur)
    SCREEN_HEIGHT=int(valeur)/2

    son1.play()
    
    pygame.quit()
    jeu.main(SCREEN_WIDTH, SCREEN_HEIGHT,d1,d2)
    sys.exit()
    
def quit_game():
    """Quitter le jeu"""
    pygame.quit()
    sys.exit()

def deck1():
    """Retourner Deck 1"""
    return 'deck1'

def deck2():
    """Retourner Deck 2"""
    return 'deck2'

def param():
    """Retourner le menu des paramètres"""
    return 'param'

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


    def draw_text(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        text_surface = font.render(self.text, True, (0, 0, 0))  # Texte noir
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))  # Affichage du texte

text_input = TextInput(400, 100, 200, 40)
# Menu principal
def main_menu():
    running = True
    show_error = False  # Variable pour gérer l'affichage du message d'erreur
    entered_text='1400'
    # Charger l'image de fond
    background_image = pygame.image.load("images\\background.png")  # Chemin vers l'image
    background_image = pygame.transform.scale(background_image, (L, H))  # Adapter à la taille de l'écran

    while running:
        # Afficher l'image de fond
        screen.blit(background_image, (0, 0))  # Dessiner l'image en haut à gauche
        
        # Afficher le titre (centré)
        title_text = font.render("CLASH OF LIFE", True, (0, 0, 0))  # Titre en noir
        title_x = (L - title_text.get_width()) // 2
        title_y = int(H * 0.05)  # Position verticale du titre (5% de la hauteur de la fenêtre)
        screen.blit(title_text, (title_x, title_y))
        
        # Paramètres des boutons (ajustés en fonction de L et H)
        button_width = int(L * 0.3)  # Largeur des boutons (30% de la largeur de la fenêtre)
        button_height = int(H * 0.07)  # Hauteur des boutons (10% de la hauteur de la fenêtre)
        button_spacing = int(H * 0.02)  # Espacement vertical entre les boutons (2% de la hauteur de la fenêtre)
        font_size = int(min(button_width, button_height) * 0.5)

        # Calcul des positions des boutons
        total_height = len(options) * button_height + (len(options) - 1) * button_spacing
        start_y = (H - total_height) // 2  # Centrage vertical des boutons
        
        # Créer des boutons
        start_button = Button("Démarrer", (L - button_width) // 2, start_y, button_width, button_height, GREEN,lambda: start_game(entered_text))
        quit_button = Button("Quitter", (L - button_width) // 2, start_y + 4 * (button_height + button_spacing) , button_width, button_height, (200, 200, 200), quit_game)
        deck_1 = Button("Deck 1", (L - button_width) // 2, start_y + 1 * (button_height + button_spacing), button_width, button_height, BLUE, lambda: deck1())
        deck_2 = Button("Deck 2", (L - button_width) // 2, start_y + 2 * (button_height + button_spacing), button_width, button_height, RED, lambda: deck2())
        parametre = Button("Paramètres", (L - button_width) // 2, start_y + 3 * (button_height + button_spacing), button_width, button_height, (200, 200, 200), lambda: param())
       
       # Affichage du message d'erreur si nécessaire
        if show_error:
            error_message = font.render("Decks non remplis", True, (255, 0, 0))  # Message en rouge
            screen.blit(error_message, (L // 2 - error_message.get_width() // 2, H // 1.1))  # Affichage du message

        # Dessiner les boutons et le champ de texte
        start_button.draw(screen, font_size)
        quit_button.draw(screen, font_size)
        deck_1.draw(screen, font_size)
        deck_2.draw(screen, font_size)
        parametre.draw(screen, font_size)
        
        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()  # On arrête Pygame
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_hovered():
                    # Vérification si les decks sont remplis
                    if len(d1) == 0 or len(d2) == 0:
                        show_error = True  # Si un deck est vide, afficher l'erreur
                    else:
                        show_error = False  # Réinitialiser l'erreur et lancer le jeu
                        start_button.click()  # Exécuter le code pour démarrer le jeu
                   
                elif quit_button.is_hovered():
                    quit_button.click()
                elif deck_1.is_hovered():
                    deck_1.click()
                    return 'deck1'
                elif deck_2.is_hovered():
                    deck_2.click()
                    return 'deck2'
                elif parametre.is_hovered():
                    parametre.click()
                    return 'param'
            result = text_input.handle_text_event(event)
            if result:
                entered_text = result
        pygame.display.update()

    return None

# Menu pour Deck 1
def Menu_deck1():
    running = True
     # Charger l'image de fond
    background_image = pygame.image.load("images\\background.png")  # Chemin vers l'image
    background_image = pygame.transform.scale(background_image, (L, H))  # Adapter à la taille de l'écran

    while running:
        # Afficher l'image de fond
        screen.blit(background_image, (0, 0))  # Dessiner l'image en haut à gauche
        # Afficher le titre principal
        title_text = font.render("Deck 1", True, BLACK)
        screen.blit(title_text, (L // 2 - title_text.get_width() // 2, H // 20))  # Centrage horizontal, position verticale à 10% de H

        # Taille des boutons
        button_width = int(L * 0.15)  # 15% de la largeur de l'écran
        button_height = int(H * 0.08)  # 8% de la hauteur de l'écran
        font_size = int(min(button_width, button_height) * 0.5)  # Taille de la police 

        # Calculer les espacements
        troupes_spacing = int(H * 0.09)  # Espacement vertical entre les boutons de troupes
        batiments_spacing = int(H * 0.1)  # Espacement vertical entre les boutons de bâtiments
        canons_spacing = int(H * 0.1)  # Espacement vertical entre les boutons de canons
        sorts_spacing = int(H * 0.1)  # Espacement vertical entre les boutons de sorts

        # Définir les positions des colonnes
        troupes_x1 = int(L * 0.1)  # Colonne 1 (Troupes, première colonne)
        troupes_x2 = int(L * 0.3)  # Colonne 2 (Troupes, deuxième colonne)
        batiments_x = int(L * 0.5)  # Colonne 3 (Bâtiments)
        canons_x = int(L * 0.7)  # Colonne 4 (Canons)
        sorts_x = canons_x  # Les sorts suivent les canons

        # Afficher les catégories
        afficher_texte(troupes_x1, H // 5 - 50, "Troupes", BLACK, 50)
        afficher_texte(batiments_x, H // 5 - 50, "Bâtiments", BLACK, 50)
        afficher_texte(canons_x, H // 5 - 50, "Canons", BLACK, 50)

        # Boutons de troupes
        troupes_buttons_col1 = [
            Button("MWSS", troupes_x1, H // 5, button_width, button_height, BLUE, lambda: ajoute(d1, "MWSS")),
            Button("BigA", troupes_x1, H // 5 + troupes_spacing, button_width, button_height, BLUE, lambda: ajoute(d1, "BigA")),
            Button("Big Glider", troupes_x1, H // 5 + 2 * troupes_spacing, button_width, button_height, BLUE, lambda: ajoute(d1, "Big_Glider")),
            Button("Dart", troupes_x1, H // 5 + 4 * troupes_spacing, button_width, button_height, BLUE, lambda: ajoute(d1, "Dart")),
            Button("Brain", troupes_x1, H // 5 + 3 * troupes_spacing, button_width, button_height, BLUE, lambda: ajoute(d1, "Brain")),
            Button("P3H", troupes_x1, H // 5 +5 * troupes_spacing, button_width, button_height, BLUE, lambda: ajoute(d1, "P3H"))
        ]

        troupes_buttons_col2 = [
            Button("Turtle", troupes_x2, H // 5, button_width, button_height, BLUE, lambda: ajoute(d1, "Turtle")),
            Button("Crab", troupes_x2, H // 5 + troupes_spacing, button_width, button_height, BLUE, lambda: ajoute(d1, "Crab")),
            Button("Lobster", troupes_x2, H // 5 + 2 * troupes_spacing, button_width, button_height, BLUE, lambda: ajoute(d1, "Lobster")),
            Button("Hivenudger", troupes_x2, H // 5 + 3 * troupes_spacing, button_width, button_height, BLUE, lambda: ajoute(d1, "Hivenudger")),
            Button("MWSSXMWSS", troupes_x2, H // 5 + 5 * troupes_spacing, button_width, button_height, BLUE, lambda: ajoute(d1, "MWSSXMWSS")),
            Button("Barge2", troupes_x2, H // 5 + 4 * troupes_spacing, button_width, button_height, BLUE, lambda: ajoute(d1, "Barge2"))
        ]

        # Boutons de bâtiments
        batiments_buttons = [
            Button("Canada Goose", batiments_x, H // 5, button_width, button_height, BLUE, lambda: ajoute(d1, "Canada_Goose")),
            Button("Queen bee", batiments_x, H // 5 + batiments_spacing, button_width, button_height, BLUE, lambda: ajoute(d1, "Queen_bee")),
            Button("P14", batiments_x, H // 5 + 2 * batiments_spacing, button_width, button_height, BLUE, lambda: ajoute(d1, "P14")),
        ]

        # Boutons de canons
        canons_buttons = [
            Button("Simkin", canons_x, H // 5, button_width, button_height, BLUE, lambda: ajoute(d1, "Simkin_glider")),
            Button("Gosper", canons_x, H // 5 + canons_spacing, button_width, button_height, BLUE, lambda: ajoute(d1, "Gosper_Glider_Gun")),
        ]

        # Titre "Sorts" juste en dessous des boutons des canons
        sorts_title_y = H // 5 + 2 * canons_spacing + int(H * 0.05)  # Légèrement espacé des canons
        afficher_texte(sorts_x, sorts_title_y, "Sorts", BLACK, 50)

        # Boutons de sorts en dessous du titre "Sorts"
        sorts_buttons = [
            Button("Pi", sorts_x, sorts_title_y + int(H * 0.08), button_width, button_height, BLUE, lambda: ajoute(d1, "Pi_heptomino")),
            Button("Wing", sorts_x, sorts_title_y + int(H * 0.08) + sorts_spacing, button_width, button_height, BLUE, lambda: ajoute(d1, "Wing")),
        ]

        # Dessiner tous les boutons
        for button in troupes_buttons_col1 + troupes_buttons_col2 + batiments_buttons + canons_buttons + sorts_buttons:
            button.draw(screen, font_size)

        # Bouton "Fini"
        fini_button = Button("Fini", canons_x, sorts_title_y + 3 * sorts_spacing, button_width, button_height, GREEN, None)
        fini_button.draw(screen, font_size)

        # Afficher la sélection au-dessus du bouton "Fini"
        afficher_selection(d1, sorts_title_y + 4 * sorts_spacing)  # 50 pixels au-dessus du bouton "Fini"


        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Vérification des clics pour chaque bouton
                for button in troupes_buttons_col1 + troupes_buttons_col2 + batiments_buttons + canons_buttons + sorts_buttons:
                    if button.is_hovered():
                        button.click()
                # Vérification du bouton "Fini"
                if fini_button.is_hovered():
                    fini_button.click()
                    return 'menu'

        # Mettre à jour l'écran
        pygame.display.update()

    return None

def afficher_selection(selected_ships, y_position):
    """Affiche un enchaînement de 5 zones bleues pour afficher les vaisseaux sélectionnés."""
    # Définir les dimensions des zones
    num_zones = 5  # Nombre de zones pour afficher les vaisseaux
    zone_width = L // 6  # Largeur d'une zone (un peu plus petite que 1/5 de la largeur de l'écran)
    zone_height = H // 10  # Hauteur de la zone

    # Définir la couleur des zones et des bordures
    zone_color = WHITE  # Bleu
    border_color = BLACK  # Noir

    # Affichage des zones
    for i in range(num_zones):
        # Calculer la position horizontale de chaque zone
        x_pos = (L // 2 - (num_zones * zone_width) // 2) + i * zone_width  # Centrage horizontal
        pygame.draw.rect(screen, zone_color, (x_pos, y_position, zone_width, zone_height))  # Zone bleue
        pygame.draw.rect(screen, border_color, (x_pos, y_position, zone_width, zone_height), 2)  # Bordure noire

        # Afficher les vaisseaux dans les zones
        if i < len(selected_ships):  # Vérifier si un vaisseau a été sélectionné pour cette zone
            ship_text = font.render(ship[selected_ships[i]], True, BLACK)  # Texte du vaisseau (en blanc)

            # Calculer la taille du texte pour qu'il tienne dans la zone
            max_text_width = zone_width - 20  # Laisser un peu de marge
            max_text_height = zone_height - 20  # Laisser un peu de marge
            font_size = min(max_text_width // len(ship[selected_ships[i]]), max_text_height)  # Ajuster la taille du texte

            # Re-créer la police avec la taille calculée
            font_resized = pygame.font.Font(None, font_size)
            ship_text_resized = font_resized.render(ship[selected_ships[i]], True, BLACK)

            # Positionner le texte au centre de la zone
            text_x = x_pos + (zone_width - ship_text_resized.get_width()) // 2
            text_y = y_position + (zone_height - ship_text_resized.get_height()) // 2
            screen.blit(ship_text_resized, (text_x, text_y))  # Afficher le texte






# Menu pour Deck 2
def Menu_deck2():

    running = True
    selected_ships = []  # Liste pour garder les vaisseaux sélectionnés
    max_selection = 5  # Limite de sélection à 5 vaisseaux
     # Charger l'image de fond
    background_image = pygame.image.load("images\\background.png")  # Chemin vers l'image
    background_image = pygame.transform.scale(background_image, (L, H))  # Adapter à la taille de l'écran

    while running:
        # Afficher l'image de fond
        screen.blit(background_image, (0, 0))  # Dessiner l'image en haut à gauche

        # Afficher le titre principal
        title_text = font.render("Deck 2", True, BLACK)
        screen.blit(title_text, (L // 2 - title_text.get_width() // 2, H // 20))  # Centrage horizontal, position verticale à 10% de H

        # Taille des boutons
        button_width = int(L * 0.15)  # 15% de la largeur de l'écran
        button_height = int(H * 0.08)  # 8% de la hauteur de l'écran
        font_size = int(min(button_width, button_height) * 0.5)  # Taille de la police 


        # Calculer les espacements
        troupes_spacing = int(H * 0.09)  # Espacement vertical entre les boutons de troupes
        batiments_spacing = int(H * 0.1)  # Espacement vertical entre les boutons de bâtiments
        canons_spacing = int(H * 0.1)  # Espacement vertical entre les boutons de canons
        sorts_spacing = int(H * 0.1)  # Espacement vertical entre les boutons de sorts

        # Définir les positions des colonnes
        troupes_x1 = int(L * 0.1)  # Colonne 1 (Troupes, première colonne)
        troupes_x2 = int(L * 0.3)  # Colonne 2 (Troupes, deuxième colonne)
        batiments_x = int(L * 0.5)  # Colonne 3 (Bâtiments)
        canons_x = int(L * 0.7)  # Colonne 4 (Canons)
        sorts_x = canons_x  # Les sorts suivent les canons

        # Afficher les catégories
        afficher_texte(troupes_x1, H // 5 - 50, "Troupes", BLACK, 50)
        afficher_texte(batiments_x, H // 5 - 50, "Bâtiments", BLACK, 50)
        afficher_texte(canons_x, H // 5 - 50, "Canons", BLACK, 50)

        # Boutons de troupes
        troupes_buttons_col1 = [
            Button("MWSS", troupes_x1, H // 5, button_width, button_height, RED, lambda: ajoute(d2, "MWSS")),
            Button("BigA", troupes_x1, H // 5 + troupes_spacing, button_width, button_height, RED, lambda: ajoute(d2, "BigA")),
            Button("Big Glider", troupes_x1, H // 5 + 2 * troupes_spacing, button_width, button_height, RED, lambda: ajoute(d2, "Big_Glider")),
            Button("Brain", troupes_x1, H // 5 + 3 * troupes_spacing, button_width, button_height, RED, lambda: ajoute(d2, "Brain")),
            Button("Dart", troupes_x1, H // 5 + 4 * troupes_spacing, button_width, button_height, RED, lambda: ajoute(d2, "Dart")),
            Button("P3H", troupes_x1, H // 5 + 5 * troupes_spacing, button_width, button_height, RED, lambda: ajoute(d2, "P3H"))
        ]

        troupes_buttons_col2 = [
            Button("Turtle", troupes_x2, H // 5, button_width, button_height, RED, lambda: ajoute(d2, "Turtle")),
            Button("Crab", troupes_x2, H // 5 + troupes_spacing, button_width, button_height, RED, lambda: ajoute(d2, "Crab")),
            Button("Lobster", troupes_x2, H // 5 + 2 * troupes_spacing, button_width, button_height, RED, lambda: ajoute(d2, "Lobster")),
            Button("Hivenudger", troupes_x2, H // 5 + 3 * troupes_spacing, button_width, button_height, RED, lambda: ajoute(d2, "Hivenudger")),
            Button("MWSSxMWSS", troupes_x2, H // 5 + 5 * troupes_spacing, button_width, button_height, RED, lambda: ajoute(d2, "MWSSxMWSS")),
            Button("Barge2", troupes_x2, H // 5 + 4 * troupes_spacing, button_width, button_height, RED, lambda: ajoute(d2, "Barge2"))
        ]

        # Boutons de bâtiments
        batiments_buttons = [
            Button("Canada Goose", batiments_x, H // 5, button_width, button_height, RED, lambda: ajoute(d2, "Canada_Goose")),
            Button("Queen bee", batiments_x, H // 5 + batiments_spacing, button_width, button_height, RED, lambda: ajoute(d2, "Queen_bee")),
            Button("P14", batiments_x, H // 5 + 2 * batiments_spacing, button_width, button_height, RED, lambda: ajoute(d2, "P14")),
        ]

        # Boutons de canons
        canons_buttons = [
            Button("Simkin Glider", canons_x, H // 5, button_width, button_height, RED, lambda: ajoute(d2, "Simkin_glider")),
            Button("Gosper Glider", canons_x, H // 5 + canons_spacing, button_width, button_height, RED, lambda: ajoute(d2, "Gosper_Glider_Gun")),
        ]

        # Titre "Sorts" juste en dessous des boutons des canons
        sorts_title_y = H // 5 + 2 * canons_spacing + int(H * 0.05)  # Légèrement espacé des canons
        afficher_texte(sorts_x, sorts_title_y, "Sorts", BLACK, 50)

        # Boutons de sorts en dessous du titre "Sorts"
        sorts_buttons = [
            Button("Pi Heptomino", sorts_x, sorts_title_y + int(H * 0.08), button_width, button_height, RED, lambda: ajoute(d2, "Pi_heptomino")),
            Button("Wing", sorts_x, sorts_title_y + int(H * 0.08) + sorts_spacing, button_width, button_height, RED, lambda: ajoute(d2, "Wing")),
        ]

        # Dessiner tous les boutons
        for button in troupes_buttons_col1 + troupes_buttons_col2 + batiments_buttons + canons_buttons + sorts_buttons:
            button.draw(screen, font_size)

        # Bouton "Fini"
        fini_button = Button("Fini", canons_x, sorts_title_y + 3 * sorts_spacing, button_width, button_height, GREEN, None)
        fini_button.draw(screen, font_size)

        # Afficher la sélection au-dessus du bouton "Fini"
        afficher_selection(d2, sorts_title_y + 4 * sorts_spacing)  # 50 pixels au-dessus du bouton "Fini"

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Vérification des clics pour chaque bouton
                for button in troupes_buttons_col1 + troupes_buttons_col2 + batiments_buttons + canons_buttons + sorts_buttons:
                    if button.is_hovered():
                        button.click()
                # Vérification du bouton "Fini"
                if fini_button.is_hovered():
                    fini_button.click()
                    return 'menu'

        # Mettre à jour l'écran
        pygame.display.update()

    return None



# Menu des paramètres


def Menu_param():
    global L, H, screen  # Déclare L et H comme variables globales pour pouvoir les modifier
    running = True

    # Charger l'image de fond
    background_image = pygame.image.load("images\\background.png")  # Chemin vers l'image
    background_image = pygame.transform.scale(background_image, (L, H))  # Adapter à la taille de l'écran

    while running:
        # Afficher l'image de fond
        screen.blit(background_image, (0, 0))  # Dessiner l'image en haut à gauche


        # Paramètres des boutons (ajustés en fonction de L et H)
        button_width = int(L * 0.3)  # Largeur des boutons (30% de la largeur de la fenêtre)
        button_height = int(H * 0.07)  # Hauteur des boutons (10% de la hauteur de la fenêtre)
        button_spacing = int(H * 0.02)  # Espacement vertical entre les boutons (2% de la hauteur de la fenêtre)
        font_size = int(min(button_width, button_height) * 0.5)


        # Afficher le titre (centré)
        title_text = font.render("Paramètres", True, (0, 0, 0))  # Titre en noir
        title_x = (L - title_text.get_width()) // 2
        title_y = int(H * 0.05)  # Position verticale du titre (5% de la hauteur de la fenêtre)
        screen.blit(title_text, (title_x, title_y))

        # Calcul des positions des boutons
        total_height = len(options) * button_height + (len(options) - 1) * button_spacing
        start_y = (H - total_height) // 2  # Centrage vertical des boutons

        buttons = []
        for i, (label, (width, height)) in enumerate(options.items()):
            button_y = start_y + i * (button_height + button_spacing)
            button = Button(
                label,
                (L - button_width) // 2,  # Centrage horizontal des boutons
                button_y,
                button_width,
                button_height,
                (200, 200, 200),
                lambda w=width, h=height: update_size(w, h)
            )
            buttons.append(button)

        # Bouton Quitter (centré sous les options)
        quit_button_y = start_y + total_height + int(H * 0.05)  # Espacement sous les boutons
        quit_button = Button(
            "Quitter",
            (L - button_width) // 2,
            quit_button_y,
            button_width,
            button_height,
            (100, 150, 200),
            lambda: "menu"
        )

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:  # Si la fenêtre est redimensionnée
                L, H = event.size  # Mettre à jour les dimensions de la fenêtre
                screen = pygame.display.set_mode((L, H), pygame.RESIZABLE)  # Redimensionner la fenêtre
                button_width = int(L * 0.3)  # Réajuster la largeur des boutons
                button_height = int(H * 0.1)  # Réajuster la hauteur des boutons
                button_spacing = int(H * 0.02)  # Réajuster l'espacement vertical entre les boutons
                font_size = int(min(button_width, button_height) * 0.5)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.is_hovered():
                    quit_button.click()
                    return "menu"
                for button in buttons:
                    if button.is_hovered():
                        button.click()

            
        # Dessiner les boutons
        for button in buttons:
            button.draw(screen, font_size)
        quit_button.draw(screen, font_size)

        pygame.display.update()

    return None

def update_size(width, height):
    """Met à jour les dimensions de l'écran."""
    global H, L, screen
    H, L = height, width
    screen = pygame.display.set_mode((L, H))  # Applique les nouvelles dimensions

# Fonction principale qui gère les scènes
def game_loop():
    current_scene = 'menu'
    while True:
        if current_scene == 'menu':
            current_scene = main_menu()
        elif current_scene == 'deck1':
            current_scene = Menu_deck1()
        elif current_scene == 'deck2':
            current_scene = Menu_deck2()
        elif current_scene == 'param':
            current_scene = Menu_param()
        elif current_scene == 'quit':
            break

    pygame.quit()
    sys.exit()

# Lancer le jeu
if __name__ == "__main__":
    game_loop()