import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('pygame event')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == '':
                print('[key down]', ' #', event.key, event.mod)
            else:
                print('[key down]', ' #', event.unicode, event.key, event.mod)
        elif event.type == pygame.MOUSEMOTION:
            print('[mouse motion]', ' #', event.pos, event.rel, event.buttons)
        elif event.type == pygame.MOUSEBUTTONUP:
            print('[mouse button up]', ' #', event.pos, event.button)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('[mouse button down]', ' #', event.pos, event.button)
    pygame.display.update()