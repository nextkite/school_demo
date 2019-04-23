import pygame
import random
from sys import exit


def prepare_bg(flag_bg):
    bg = ["./background/background_1.png",
          "./background/background_2.png",
          "./background/background_3.png",
          "./background/background_4.png"]

    pygame.init()
    screen = pygame.display.set_mode((600, 800), 0, 32)
    for i in range(0, 3):
        bg[i] = pygame.image.load(bg[i])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.blit(bg[flag_bg], (0, 0))
        screen.blit(bg[flag_bg], (300, 0))
        screen.blit(bg[flag_bg], (0, 300))
        screen.blit(bg[flag_bg], (300, 300))
        screen.blit(bg[flag_bg], (0, 600))
        screen.blit(bg[flag_bg], (300, 600))

        pygame.display.update()




if __name__ == "__main__":
    prepare_bg(2)
