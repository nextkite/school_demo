import pygame
import random
from sys import exit

bg = './images/background.png'
me = './images/me.png'
me_d1 = './images/me_destroy_1.png'
me_d2 = './images/me_destroy_2.png'
me_d3 = './images/me_destroy_3.png'
bullet = './images/bullet1.png'
enemy = './images/enemy1.png'
e_d1 = './images/enemy1_down1.png'
e_d2 = './images/enemy1_down2.png'
e_d3 = './images/enemy1_down3.png'
again = './images/again.png'
gameover = './images/gameover.png'

arr_bullet = []
arr_enemy = []
Y = 0
me_flag = 1
again_flag = 0
m_x = 0
m_y = 0


def update():
    global Y
    global m_x
    global m_y
    global me_flag
    global again
    global gameover
    # 将背景画上去
    screen.blit(bg, (0, Y - 700))
    screen.blit(bg, (0, Y))
    # 获取鼠标位置,将飞机画上去
    m_x, m_y = pygame.mouse.get_pos()
    m_x = m_x - me.get_width() / 2
    m_y = m_y - me.get_width() / 2
    if me_flag == 1:
        screen.blit(me, (m_x, m_y))
    # 将子弹画上去
    for i in arr_bullet:
        x, y = i
        screen.blit(bullet, (x, y))
    # 将敌机画上去
    for i in arr_enemy:
        x, y, v = i
        screen.blit(enemy, (x, y))

    # 子弹弹道
    k = len(arr_bullet)
    for i in range(0, k):
        x, y = arr_bullet[i]
        arr_bullet[i] = (x, y - 2)

    # 敌机轨迹
    if (Y % 150) == 0:
        x = random.randint(30, 450)
        y = random.randint(-50, -5)
        v = random.randint(1, 6)
        if v == 1:
            v = 1
        elif v == 2 or v == 3 or v == 4 or v == 5:
            v = 1.5
        elif v == 6:
            v = 3
        arr_enemy.append((x, y, v))

    k = len(arr_enemy)
    for i in range(0, k):
        x, y, v = arr_enemy[i]
        arr_enemy[i] = (x, y + v, v)

    if me_flag == 0:
        screen.blit(again, (100, 300))
        screen.blit(gameover, (100, 350))


    pygame.display.update()



    # 周期计时器
    Y = Y + 1
    if Y > 700:
        Y = 0


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((480, 700), 0, 32)
    pygame.display.set_caption("Fly!!!")
    bg = pygame.image.load(bg)  # 背景图片
    me = pygame.image.load(me)  # 我的飞机
    me_d1 = pygame.image.load(me_d1)
    me_d2 = pygame.image.load(me_d2)
    me_d3 = pygame.image.load(me_d3)
    bullet = pygame.image.load(bullet)  # 子弹
    enemy = pygame.image.load(enemy)  # 敌机
    e_d1 = pygame.image.load(e_d1)
    e_d2 = pygame.image.load(e_d2)
    e_d3 = pygame.image.load(e_d3)
    again = pygame.image.load(again)
    gameover = pygame.image.load(gameover)

    while True:

        # 捕获事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and me_flag == 1:
                x, y = pygame.mouse.get_pos()
                arr_bullet.append((x, y - 55))
            if event.type == pygame.MOUSEBUTTONDOWN and me_flag == 0:
                x, y = pygame.mouse.get_pos()
                if 100 < x and x <400 and  300 < y and y < 341:
                    me_flag = 1
                    arr_enemy.clear()
                elif 100 < x and x <400 and  350 < y and y < 391:
                    exit()


        update()

        # 子弹与敌机相撞事件
        k_b = len(arr_bullet)
        for i in range(k_b - 1, -1, -1):
            x_b, y_b = arr_bullet[i]
            x_b = x_b + 2

            flag = 0
            k_e = len(arr_enemy)
            for j in range(k_e - 1, -1, -1):
                x_e, y_e, v_e = arr_enemy[j]
                x_e = x_e + 28
                if abs(x_b - x_e) < 40 and y_b - y_e < 10 and y_b - y_e > 0:
                    flag = 1
                    del arr_enemy[j]
                    break

            if flag == 1:
                del arr_bullet[i]

                for i in range(0, 20):
                    screen.blit(e_d1, (x_e - 28, y_e - 5))
                    pygame.display.update()

                update()

                for i in range(0, 20):
                    screen.blit(e_d2, (x_e - 28, y_e - 5))
                    pygame.display.update()
                update()

                for i in range(0, 50):
                    screen.blit(e_d3, (x_e - 28, y_e - 5))
                    pygame.display.update()
                update()

        # 敌机与我机相撞
        if me_flag == 1:
            update()
            k_e = len(arr_enemy)
            for i in range(k_e - 1, -1, -1):
                t_m_x, t_m_y = pygame.mouse.get_pos()
                x_e, y_e, v_e = arr_enemy[i]
                x_e = x_e + 28
                if (abs(t_m_x - x_e) < 40 and t_m_y - y_e < 90 and t_m_y - y_e > -60) or (abs(t_m_x - x_e) < 70 and t_m_y - y_e < 40 and t_m_y - y_e > -60):
                    me_flag = 0
                    del arr_enemy[i]

                    for i in range(0, 20):
                        screen.blit(e_d1, (x_e - 28, y_e - 5))
                        screen.blit(me_d1, (m_x, m_y))
                        pygame.display.update()
                    update()

                    for i in range(0, 20):
                        screen.blit(e_d2, (x_e - 28, y_e - 5))
                        screen.blit(me_d2, (m_x, m_y))
                        pygame.display.update()
                    update()

                    for i in range(0, 50):
                        screen.blit(e_d3, (x_e - 28, y_e - 5))
                        screen.blit(me_d3, (m_x, m_y))
                        pygame.display.update()
                    update()

                    break

        # 删除越界子弹
        k = len(arr_bullet)
        for i in range(k - 1, -1, -1):
            x, y = arr_bullet[i]
            if y <= 0:
                del arr_bullet[i]

        # 删除越界敌机
        k = len(arr_enemy)
        for i in range(k - 1, -1, -1):
            x, y, v = arr_enemy[i]
            if y > 700:
                del arr_enemy[i]
