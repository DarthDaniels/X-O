import time

import pygame
from time import sleep
from random import randint

pygame.init()

game_field = [['', '', ''],
              ['', '', ''],
              ['', '', '']]

SIZE = (600, 600)
color_bg = [255, 255, 255]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Крестики и Нолики")

fps = 60
clock = pygame.time.Clock()
step = False

state = "menu"
f1 = pygame.font.Font(None, 36)
text1 = f1.render('Нажмите ПРОБЕЛ чтобы продолжить', True, (49, 20, 30))


def check_line(string, matrix, ch_line, ch_all=False):
    """

    :param string: "xxx"
    :param matrix: [0, 1, 0], [0, 1, 0], [0, 1, 0]
    :param ch_all: True -> проверить все линии
    :param ch_line:
    :return:
    """
    if not ch_line:
        indexes = []
        out = []
        for line in range(3):
            for elem in range(3):
                if matrix[line][elem]:
                    indexes.append([line, elem])

        real_string = ""
        for i in indexes:
            real_string += game_field[i[0]][i[1]]
            out.append(i[0])
            out.append(i[1])
            print(out)
            print(real_string + "!!!" + string)

        return out if real_string == string else []
    if ch_line:
        if matrix[0][0] and matrix[0][1] and matrix[0][2] or ch_all:
            if game_field[0][0] + game_field[0][1] + game_field[0][2] == string:
                return [0, 0, 0, 1, 0, 2]
        if matrix[1][0] and matrix[1][1] and matrix[1][2] or ch_all:
            if game_field[1][0] + game_field[1][1] + game_field[1][2] == string:
                return [1, 0, 1, 1, 1, 2]
        if matrix[2][0] and matrix[2][1] and matrix[2][2] or ch_all:
            if game_field[2][0] + game_field[2][1] + game_field[2][2] == string:
                return [2, 0, 2, 1, 2, 2]

        if matrix[0][0] and matrix[1][1] and matrix[2][2] or ch_all:
            if game_field[0][0] + game_field[1][1] + game_field[2][2] == string:
                return [0, 0, 1, 1, 2, 2]
        if matrix[0][2] and matrix[1][1] and matrix[2][0] or ch_all:
            if game_field[0][2] + game_field[1][1] + game_field[2][0] == string:
                return [0, 2, 1, 1, 2, 0]

        if matrix[0][0] and matrix[1][0] and matrix[2][0] or ch_all:
            if game_field[0][0] + game_field[1][0] + game_field[2][0] == string:
                return [0, 0, 1, 0, 2, 0]
        if matrix[0][1] and matrix[1][1] and matrix[2][1] or ch_all:
            if game_field[0][1] + game_field[1][1] + game_field[2][1] == string:
                return [0, 1, 1, 1, 2, 1]
        if matrix[0][2] and matrix[1][2] and matrix[2][2] or ch_all:
            if game_field[0][2] + game_field[1][2] + game_field[2][2] == string:
                return [0, 2, 1, 2, 2, 2]
        return []


def show_field():
    """
    Функция отображения игрового поля.
    :return: None
    """
    screen.fill(color_bg)
    pygame.draw.line(screen, (0, 0, 0), [200, 0], [200, 600], 5)
    pygame.draw.line(screen, (0, 0, 0), [400, 0], [400, 600], 5)
    pygame.draw.line(screen, (0, 0, 0), [0, 200], [600, 200], 5)
    pygame.draw.line(screen, (0, 0, 0), [0, 400], [600, 400], 5)

    for line in range(len(game_field)):
        for elem in range(len(game_field[line])):
            if game_field[line][elem] == 'x':
                """pygame.draw.line(screen, (200, 0, 0), [200 * elem, 200 * line], [200 * elem + 200, 200 * line + 200], 5)
                   pygame.draw.line(screen, (200, 0, 0), [200 * elem + 200, 200 * line], [200 * elem, 200 * line + 200], 5)"""
                pygame.draw.line(screen, (200, 0, 0), [200*elem+50, 200*line+50],
                                 [200*elem+200-50, 200*line+200-50], 10)
                pygame.draw.line(screen, (200, 0, 0), [200 * elem + 150, 200 * line + 50],
                                 [200 * elem + 200 - 150, 200 * line + 200 - 50], 10)

            if game_field[line][elem] == 'o':
                pygame.draw.circle(screen, (0, 0, 200), [200 * elem + 100, 200 * line + 100], 50, 10)


def computer_step():
    """
    Алгоритм действий программы
    :return: None
    """
    time.sleep(1)
    if game_field[1][1] == '':
        print(1)
        game_field[1][1] = 'o'
        return

    # ooo
    cur = check_line("oo", [['', '', ''], ['', '', ''], ['', '', '']], True, True)
    if len(cur) == 6:
        print(2)
        if game_field[cur[0]][cur[1]] == '':
            game_field[cur[0]][cur[1]] = 'o'
            return
        if game_field[cur[2]][cur[3]] == '':
            game_field[cur[2]][cur[3]] = 'o'
            return
        if game_field[cur[4]][cur[5]] == '':
            game_field[cur[4]][cur[5]] = 'o'
            return
    # xxo
    cur = check_line("xx", [['', '', ''], ['', '', ''], ['', '', '']], True, True)
    if len(cur) == 6:
        print(3)
        if game_field[cur[0]][cur[1]] == '':
            game_field[cur[0]][cur[1]] = 'o'
            return
        if game_field[cur[2]][cur[3]] == '':
            game_field[cur[2]][cur[3]] = 'o'
            return
        if game_field[cur[4]][cur[5]] == '':
            game_field[cur[4]][cur[5]] = 'o'
            return

    if check_line("xox", [[1, 0, 0], [0, 1, 0], [0, 0, 1]], True) or \
            check_line("xox", [[0, 0, 1], [0, 1, 0], [1, 0, 0]], True):
        print(4)
        if game_field[2][1] == '':
            game_field[2][1] = 'o'
            return
        if game_field[0][1] == '':
            game_field[0][1] = 'o'
            return
        if game_field[1][2] == '':
            game_field[1][2] = 'o'
            return
        if game_field[1][0] == '':
            game_field[1][0] = 'o'
            return

    if check_line("x", [[1, 1, 1], [0, 0, 0], [0, 0, 0]], True) and \
            check_line("x", [[0, 0, 0], [1, 0, 0], [1, 0, 0]], False):
        print(5)
        if game_field[0][0] == '':
            game_field[0][0] = 'o'
            return
        if game_field[0][1] == '':
            game_field[0][1] = 'o'
            return
        if game_field[1][0] == '':
            game_field[1][0] = 'o'
            return

    if check_line("x", [[1, 1, 1], [0, 0, 0], [0, 0, 0]], True) and \
            check_line("x", [[0, 0, 0], [0, 0, 1], [0, 0, 1]], False):
        print(6)
        if game_field[0][2] == '':
            game_field[0][2] = 'o'
            return
        if game_field[1][2] == '':
            game_field[1][2] = 'o'
            return
        if game_field[0][1] == '':
            game_field[0][1] = 'o'
            return

    if check_line("x", [[0, 0, 0], [0, 0, 0], [1, 1, 1]], True) and \
            check_line("x", [[0, 0, 1], [0, 0, 1], [0, 0, 0]], False):
        print(7)
        if game_field[2][2] == '':
            game_field[2][2] = 'o'
            return
        if game_field[1][2] == '':
            game_field[1][2] = 'o'
            return
        if game_field[2][1] == '':
            game_field[2][1] = 'o'
            return

    if check_line("x", [[0, 0, 0], [0, 0, 0], [1, 1, 1]], True) and \
            check_line("x", [[1, 0, 0], [1, 0, 0], [0, 0, 0]], False):
        print(8)
        if game_field[2][0] == '':
            game_field[2][0] = 'o'
            return
        if game_field[1][0] == '':
            game_field[1][0] = 'o'
            return
        if game_field[2][1] == '':
            game_field[2][1] = 'o'
            return

    if game_field[0][0] == '':
        game_field[0][0] = 'o'
        return
    if game_field[0][2] == '':
        game_field[0][2] = 'o'
        return
    if game_field[2][0] == '':
        game_field[2][0] = 'o'
        return
    if game_field[2][2] == '':
        game_field[2][2] = 'o'
        return

    for line in range(3):
        for elem in range(3):
            if game_field[line][elem] == '':
                game_field[line][elem] = 'o'
                return


def usr_step(mouse_position, mouse_clicked):
    """
    Функция записи хода игрока на поле
    :param mouse_position: позиция мыши
    :param mouse_clicked: проверка нажатия кнопки мыши
    :return: bool
    """
    x, y = 0, 0
    if mouse_position[0] <= 200:
        x = 0
    elif mouse_position[0] <= 400:
        x = 1
    elif mouse_position[0] <= 600:
        x = 2

    if mouse_position[1] <= 200:
        y = 0
    elif mouse_position[1] <= 400:
        y = 1
    elif mouse_position[1] <= 600:
        y = 2

    if mouse_clicked:
        if game_field[y][x] == '':
            game_field[y][x] = 'x'
            return True
    return False


run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

    if state == "menu":
        screen.fill(color_bg)
        screen.blit(text1, (50, 260))############################
        for event in events:
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                state = "game"
    if state == "game":
        show_field()

        if not step:
            clicked = False
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    clicked = True
            if usr_step(pygame.mouse.get_pos(), clicked):
                step = True
        else:
            pygame.display.update()
            computer_step()
            step = False

        places = 9
        for i in range(3):
            for j in range(3):
                if game_field[i][j] != '':
                    places -= 1

        if check_line("xxx", [['', '', ''], ['', '', ''], ['', '', '']], True, True) or \
                check_line("ooo", [['', '', ''], ['', '', ''], ['', '', '']], True, True) or places == 0:
            state = "menu"
            game_field = [['', '', ''],
                          ['', '', ''],
                          ['', '', '']]

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
