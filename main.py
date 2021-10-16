import pygame


BUTTON_COLOR_OFF = (100, 100, 150)
BUTTON_COLOR_ON = (150, 150, 100)
FPS = 60

pygame.init()

clock = pygame.time.Clock()

display = pygame.display.set_mode((1050, 650))
display.fill(color=(255, 255, 255))
pygame.display.set_caption('Drawing digits')

text_main = pygame.font.SysFont('arial', 20)
text_surface = text_main.render('Нарисуйте цифру', True, (0, 0, 0))

surf = pygame.Surface((28*15, 28*15))
surf.fill((0, 0, 0))
display.blit(surf, (50, 50))
display.blit(text_surface, (185, 20))
pygame.display.update()


class BigPixel:
    def __init__(self):
        ...

    def one_pixel(self):
        ...


def run_game():
    flag = True

    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('STOP')
                exit()

            mouse = pygame.mouse.get_pos()

            if 50 < mouse[0] < 50+150 and 500 < mouse[1] < 500+50:
                button_clear = pygame.draw.rect(display, BUTTON_COLOR_ON, (50, 500, 150, 50))
            elif 320 < mouse[0] < 320+150 and 500 < mouse[1] < 500+50:
                button_get = pygame.draw.rect(display, BUTTON_COLOR_ON, (320, 500, 150, 50))
            else:
                button_clear = pygame.draw.rect(display, BUTTON_COLOR_OFF, (50, 500, 150, 50))
                button_get = pygame.draw.rect(display, BUTTON_COLOR_OFF, (320, 500, 150, 50))

            text_button = pygame.font.SysFont('arial', 15)
            text_button_clear_surface = text_button.render('ОЧИСТИТЬ', True, (0, 0, 0))
            text_button_get_surface = text_button.render('ОПРЕДЕЛИТЬ ЦИФРУ', True, (0, 0, 0))

            display.blit(text_button_clear_surface, (85, 515))
            display.blit(text_button_get_surface, (330, 515))
            pygame.display.update()
            clock.tick(FPS)


run_game()
