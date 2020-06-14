import pygame
import Setup
Setup

pygame.init()
pygame.mixer.init()

fundo_1 = pygame.image.load("Sprites/Fundo1.png").convert()
kleber = pygame.image.load("Sprites/Kléber64x64.png").convert_alpha()
kleber = pygame.transform.scale2x(kleber)
jorge = pygame.image.load("Sprites/Jorge64x64.png").convert_alpha()
jorge = pygame.transform.scale2x(jorge)
heart = {
    100: pygame.image.load("Sprites/HeartFull.png").convert_alpha(),
    75: pygame.image.load("Sprites/Heart75.png").convert_alpha(),
    50: pygame.image.load("Sprites/Heart50.png").convert_alpha(),
    25: pygame.image.load("Sprites/Heart25.png").convert_alpha(),
    0: pygame.image.load("Sprites/Heart0.png").convert_alpha()
}