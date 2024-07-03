import pygame
import time

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
grey = (200, 200, 200)
dark_green = (0, 200, 0)
dark_blue = (0, 0, 200)

pygame.init()
largura = 1000
altura = 600
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Maze Solver")
window.fill(green)

cell_size = 50
now_cell = 0

cell_cords = []
borders_cords = []
# Defines The Maze
borders_map = [(22, 1), (23, 1), (43, 1), (42, 1), (21, 1), (20, 0), (10, 0), (1, 1), (2, 1), (4, 1), (5, 1), (6, 1), (8, 1), (9, 1), (31, 1), (30, 1), (12, 0), (22, 0), (23, 0), (13, 0), (24, 1), (25, 1), (16, 0), (17, 0), (27, 0), (37, 0), (47, 0), (67, 0), (77, 0), (97, 0), (97, 1), (96, 1), (95, 1), (94, 1), (93, 1), (92, 1), (91, 1), (90, 1), (98, 1), (99, 1), (99, 0), (89, 0), (79, 0), (69, 0), (59, 0), (49, 0), (39, 0), (29, 0), (19, 0), (9, 0), (48, 1), (48, 0), (38, 0), (18, 0), (58, 1), (59, 1), (78, 1), (78, 0), (68, 0), (88, 1), (36, 1), (36, 0), (45, 1), (44, 0), (44, 1), (46, 0), (56, 0), (56, 1), (55, 1), (53, 0), (73, 0), (74, 1), (75, 1), (77, 1), (85, 0), (87, 1), (85, 1), (84, 1), (83, 1), (72, 0), (62, 0), (52, 1), (51, 1), (50, 0), (61, 1), (71, 0), (81, 0), (81, 1), (80, 1), (70, 0), (82, 0), (0, 1), (31, 1), (31, 0), (43, 0), (33, 1), (34, 0), (75, 0), (65, 0)]
# Win Spot
win_cells_map = [43]

font = pygame.font.Font(None, 36)

map_size = (500, 500)
cell_x_map = (largura - map_size[0]) / 2
cell_y_map = (altura - map_size[1]) / 2
map_area = (cell_x_map + map_size[0], cell_y_map + map_size[1])

def draw_scene():
    global cell_cords

    for y in range(int(map_size[1] / 50)):
        for x in range(int(map_size[0] / 50)):
            pygame.draw.rect(window, grey, (cell_x_map + 50 * x, cell_y_map + 50 * y, cell_size, cell_size))
            pygame.draw.rect(window, blue, (cell_x_map + 50 * x, cell_y_map + 50 * y, cell_size, cell_size), 1)
            text = font.render(str(mouse_array_map[x + 10 * y]), True, dark_green)
            window.blit(text, ((cell_x_map + 50 * x) + 10, (cell_y_map + 50 * y) + 10))
            cell_cords.append(((cell_x_map + 50 * x) + cell_size / 2, (cell_y_map + 50 * y + cell_size / 2)))

    make_win_course()
    make_borders_course()

    pygame.draw.rect(window, black, ((largura - map_size[0]) / 2, (altura - map_size[1]) / 2, map_size[0], map_size[1]), 2)


def make_borders(cell, side):
    global borders_cords

    if side == 0:
        border_size = (4, cell_size)
        border_cord = ((cell_cords[cell][0] + cell_size / 2) - border_size[0] / 2, cell_cords[cell][1] - cell_size / 2)
        pygame.draw.rect(window, red, (border_cord[0], border_cord[1], border_size[0], border_size[1]))
        borders_cords.append((border_cord[0], border_cord[1], border_size[0], border_size[1]))

    elif side == 1:
        border_size = (cell_size, 4)
        border_cord = ((cell_cords[cell][0] - cell_size / 2), (cell_cords[cell][1] + cell_size / 2) - border_size[1] / 2)
        pygame.draw.rect(window, red, (border_cord[0], border_cord[1], border_size[0], border_size[1]))
        borders_cords.append((border_cord[0], border_cord[1], border_size[0], border_size[1]))


def make_borders_course():
    for border in borders_map:
        make_borders(border[0], border[1])


def make_win_course():
    for win_cell in win_cells_map:
        pygame.draw.rect(window, dark_green, (cell_cords[win_cell][0] - cell_size / 2, cell_cords[win_cell][1] - cell_size / 2, cell_size, cell_size))


def get_cell(cords):
    cell_num = -1
    pygame.draw.rect(window, green, (cords[0], cords[1], 5, 5))
    for cell in cell_cords:
        cell_num += 1
        actual_cord = (cell[0] - 25, cell[1] - 25)
        for x_cell in range(cell_size):
            x_cord = actual_cord[0]
            x_cord += x_cell
            for y_cell in range(cell_size):
                y_cord = actual_cord[1]
                y_cord += y_cell
                if (x_cord, y_cord) == cords:
                    print(cell_num)
                    return cell_num


def get_borders_on_cell(cell):
    on_borders = [0, 0, 0, 0]
    for borders in borders_map:
        if borders[0] == cell:
            if borders[1] == 0:
                on_borders[1] = 1
            if borders[1] == 1:
                on_borders[2] = 1
        if borders[0] == cell - 1 and borders[1] == 0:
            on_borders[0] = 1
        if borders[0] == cell - 10 and borders[1] == 1:
            on_borders[3] = 1
    return on_borders

mouse_array_map = []


def reload_array():
    global mouse_array_map
    mouse_array_map = []
    for n in range(100):
        mouse_array_map.append(101)

reload_array()


class MicroMouse:
    def __init__(self):
        self.mouse_cords = (0, 0)
        self.mouse_cell = get_cell(self.mouse_cords)

    def create_array(self):
        for win_cell in win_cells_map:
            mouse_array_map[win_cell] = 0
        num_vezes = 0
        for cell_num in range(100):
            for cell in range(len(mouse_array_map)):
                block_borders = get_borders_on_cell(cell)
                if mouse_array_map[cell] == cell_num:
                    num_vezes += 1
                    if cell > 0 and cell % 10 != 0 and mouse_array_map[cell - 1] == 101 and block_borders[0] == 0:
                        mouse_array_map[cell - 1] = cell_num + 1
                    if cell < 99 and cell % 10 != 9 and mouse_array_map[cell + 1] == 101 and block_borders[1] == 0:
                        mouse_array_map[cell + 1] = cell_num + 1
                    if cell > 9 and mouse_array_map[cell - 10] == 101 and block_borders[3] == 0:
                        mouse_array_map[cell - 10] = cell_num + 1
                    if cell < 90 and mouse_array_map[cell + 10] == 101 and block_borders[2] == 0:
                        mouse_array_map[cell + 10] = cell_num + 1

        for i in range(10):
            mouse_array = mouse_array_map[i * 10:(i + 1) * 10]

    def mouse_move(self):
        global now_cell
        borders_on = get_borders_on_cell

        pygame.draw.circle(window, dark_blue, cell_cords[now_cell], cell_size / 4)
        if borders_on(now_cell)[1] == 0 and now_cell % 10 != 9 and mouse_array_map[now_cell + 1] == mouse_array_map[now_cell] - 1:
            now_cell += 1
        elif borders_on(now_cell)[2] == 0 and now_cell <= 89 and mouse_array_map[now_cell + 10] == mouse_array_map[now_cell] - 1:
            now_cell += 10
        elif borders_on(now_cell)[0] == 0 and now_cell % 10 != 0 and mouse_array_map[now_cell - 1] == mouse_array_map[now_cell] - 1:
            now_cell -= 1
        elif borders_on(now_cell)[3] == 0 and now_cell >= 10 and mouse_array_map[now_cell - 10] == mouse_array_map[now_cell] - 1 :
            now_cell -= 10
        if mouse_array_map[now_cell] == 0:
            now_cell = 0

microMouse = MicroMouse()
window_open = True
while window_open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if cell_x_map <= pygame.mouse.get_pos()[0] <= map_area[0] and cell_y_map <= pygame.mouse.get_pos()[1] <= map_area[1]:
                    print(get_borders_on_cell(get_cell(pygame.mouse.get_pos())))
            if event.button == 3:
                if cell_x_map <= pygame.mouse.get_pos()[0] <= map_area[0] and cell_y_map <= pygame.mouse.get_pos()[1] <= map_area[1]:
                    now_cell = get_cell(pygame.mouse.get_pos())

    draw_scene()
    microMouse.create_array()
    microMouse.mouse_move()
    pygame.display.flip()
    time.sleep(0.2)
