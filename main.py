import pygame

pygame.init()

display = pygame.display.set_mode((1050, 650))
pygame.display.set_caption('Drawing digits')


def run_game():
    flag = True

    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('STOP')
                exit()

        display.fill(color=(255, 255, 255))
        pygame.display.update()


run_game()
