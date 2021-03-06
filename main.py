from neural_net import prediction_model
import pygame
import numpy as np


BUTTON_COLOR_OFF = (100, 100, 150)
BUTTON_COLOR_ON = (150, 150, 100)
FPS = 180

pygame.init()

clock = pygame.time.Clock()

display = pygame.display.set_mode((1050, 650))
display.fill(color=(200, 200, 200))
pygame.display.set_caption('Drawing digits')

text_main = pygame.font.SysFont('arial', 20)
text_surface = text_main.render('Нарисуйте цифру', True, (0, 0, 0))


def new_surf():
    surf = pygame.Surface((28 * 15, 28 * 15))
    surf.fill((0, 0, 0))
    display.blit(surf, (50, 50))
    display.blit(text_surface, (185, 20))

    for i in range(0, 29):
        pygame.draw.aaline(display, (255, 255, 255), [50 + 15 * i, 50], [50 + 15 * i, 470])
        pygame.draw.aaline(display, (255, 255, 255), [50, 50 + 15 * i], [470, 50 + 15 * i])


def one_pixel(arr):
    array_pixel = []
    for i in range(28):
        row = arr[i*15:(i+1)*15, :]
        s = []
        for j in range(28):
            el = row[:, j*15:(j+1)*15]
            if (np.sum(el)//16777215)/225 > 0.5:
                s.append(1)
            else:
                s.append(0)
        array_pixel.append(s)
    return np.array(array_pixel)


new_surf()
pygame.display.update()


def run_game():
    flag = True

    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('STOP')
                exit()

            mouse = pygame.mouse.get_pos()

            if 50 < mouse[0] < 50 + 150 and 500 < mouse[1] < 500 + 50:
                pygame.draw.rect(display, BUTTON_COLOR_ON, (50, 500, 150, 50))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    new_surf()

            elif 320 < mouse[0] < 320 + 150 and 500 < mouse[1] < 500 + 50:
                pygame.draw.rect(display, BUTTON_COLOR_ON, (320, 500, 150, 50))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    ar = pygame.PixelArray(display)
                    ar.close()
                    ara = np.array(ar)
                    ans = one_pixel(ara[50:470, 50:470]).transpose()
                    ans = ans.flatten()
                    dig, prob = prediction_model(ans)
                    # здесь будет функция отрисовки ответа

            else:
                pygame.draw.rect(display, BUTTON_COLOR_OFF, (50, 500, 150, 50))
                pygame.draw.rect(display, BUTTON_COLOR_OFF, (320, 500, 150, 50))

            text_button = pygame.font.SysFont('arial', 15)
            text_button_clear_surface = text_button.render('ОЧИСТИТЬ', True, (0, 0, 0))
            text_button_get_surface = text_button.render('ОПРЕДЕЛИТЬ ЦИФРУ', True, (0, 0, 0))

            display.blit(text_button_clear_surface, (85, 515))
            display.blit(text_button_get_surface, (330, 515))

            if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1 and \
                    70 <= mouse[0] <= 450 and 70 <= mouse[1] <= 450:
                pygame.draw.circle(display, (255, 255, 255), mouse, 20)

            pygame.display.update()
            clock.tick(FPS)


run_game()
