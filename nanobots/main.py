import pygame
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de l'écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Création de l'écran
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simulation de nanobots")

# Classe pour les nanobots
class Nanobot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)

    # Fonction pour mettre à jour la position du nanobot
    def update(self):
        self.x += self.vx
        self.y += self.vy

        # Rebondir sur les bords de l'écran
        if self.x < 0 or self.x > SCREEN_WIDTH:
            self.vx *= -1
        if self.y < 0 or self.y > SCREEN_HEIGHT:
            self.vy *= -1

    # Fonction pour afficher le nanobot
    def draw(self):
        pygame.draw.circle(screen, random.choice([WHITE, RED]), (int(self.x), int(self.y)), 5)

# Liste pour stocker les nanobots
nanobots = []

# Création des nanobots
for i in range(500):
    nanobots.append(Nanobot(random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT)))

# Boucle principale du jeu
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Effacer l'écran
    screen.fill(BLACK)

    # Mettre à jour et afficher les nanobots
    for nanobot in nanobots:
        nanobot.update()
        nanobot.draw()

    # Rafraîchir l'écran
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
