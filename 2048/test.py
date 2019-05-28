import pygame
import random
from sys import exit

score = 0  # 记录游戏分数
matix = [[0 for i in range(4)] for i in range(4)]  # 初始化生成一个4*4的列表

def init_image():
    global grid_bg
    global num_2
    global num_4
    global num_8
    global num_16
    global num_32
    global num_64
    global num_128
    global num_256
    global num_512
    global num_1024
    global num_2048
    global left
    global right
    global down
    global up
    global num_pos

    grid_bg = './image_2048/grid_bg.png'
    num_2 = './image_2048/num_2.png'
    num_4 = './image_2048/num_4.png'
    num_8 = './image_2048/num_8.png'
    num_16 = './image_2048/num_16.png'
    num_32 = './image_2048/num_32.png'
    num_64 = './image_2048/num_64.png'
    num_128 = './image_2048/num_128.png'
    num_256 = './image_2048/num_256.png'
    num_512 = './image_2048/num_512.png'
    num_1024 = './image_2048/num_1024.png'
    num_2048 = './image_2048/num_2048.png'
    left = './image_2048/left.png'
    right = './image_2048/right.png'
    down = './image_2048/down.png'
    up = './image_2048/up.png'

    grid_bg = pygame.image.load(grid_bg)
    num_2 = pygame.image.load(num_2)
    num_4 = pygame.image.load(num_4)
    num_8 = pygame.image.load(num_8)
    num_16 = pygame.image.load(num_16)
    num_32 = pygame.image.load(num_32)
    num_64 = pygame.image.load(num_64)
    num_128 = pygame.image.load(num_128)
    num_256 = pygame.image.load(num_256)
    num_512 = pygame.image.load(num_512)
    num_1024 = pygame.image.load(num_1024)
    num_2048 = pygame.image.load(num_2048)
    left = pygame.image.load(left)
    right = pygame.image.load(right)
    down = pygame.image.load(down)
    up = pygame.image.load(up)

    num_pos = [[[96, 96], [243, 96], [390, 96], [536, 96]],
           [[96, 243], [243, 243], [390, 243], [536, 243]],
           [[96, 390], [243, 390], [390, 390], [536, 390]],
           [[96, 536], [243, 536], [390, 536], [536, 536]]]

def display():
    for i in range(4):
        for j in range(4):
            if matix[i][j] != 0:
                i_str = 'num_' + str(matix[i][j])
                x, y = num_pos[i][j]
                screen.blit(eval(i_str), (x, y))

# 初始化矩阵
def init():
    initNumFlag = 0
    while 1:
        k = 2 if random.randrange(0, 10) > 1 else 4  # 随机生成 2 或 4
        s = divmod(random.randrange(0, 16), 4)  # 生成矩阵初始化的下标
        if matix[s[0]][s[1]] == 0: # 只有当其值不为0的时候才赋值，避免第二个值重复
            matix[s[0]][s[1]] = k
            initNumFlag += 1
            if initNumFlag == 2:
                break

def addRandomNum(): # 处理完移动后添加一个新的随机数

    flag = False

    for i in range(4):
        for j in range(4):
            if matix[i][j] == 0:
                flag = True

    while flag:
        g_x = random.randint(0, 3)
        g_y = random.randint(0, 3)

        if matix[g_x][g_y] == 0:
            flag = False
            matix[g_x][g_y] = random.randint(1, 2) * 2


# 检查游戏是否GG
def check():
    for i in range(4):
        for j in range(4):
            if matix[i][j] == 0:
                return True
            temp_x = i + 1
            temp_y = j + 0
            if 0 <= temp_x < 4 and 0 <= temp_y < 4 and matix[i][j] == matix[temp_x][temp_y]:
                return True

            temp_x = i + 0
            temp_y = j + 1
            if 0 <= temp_x < 4 and 0 <= temp_y < 4 and matix[i][j] == matix[temp_x][temp_y]:
                return True

            temp_x = i - 1
            temp_y = j + 0
            if 0 <= temp_x < 4 and 0 <= temp_y < 4 and matix[i][j] == matix[temp_x][temp_y]:
                return True

            temp_x = i + 0
            temp_y = j - 1
            if 0 <= temp_x < 4 and 0 <= temp_y < 4 and matix[i][j] == matix[temp_x][temp_y]:
                return True

    print("sdfsdfsdfsdfs")
    return False


def moveRight(): # 向右移动处理函数　
    global score
    for i in range(4):
        for j in range(3, 0, -1):
            for k in range(j - 1, -1, -1):
                if matix[i][k] > 0:
                    if matix[i][j] == 0:
                        matix[i][j] = matix[i][k]
                        matix[i][k] = 0
                    elif matix[i][j] == matix[i][k]:
                        matix[i][j] *= 2
                        score += matix[i][j] # 将当前数作为score加上
                        matix[i][k] = 0
                    break
    addRandomNum()

def moveUp():
    global score
    for i in range(4):
        for j in range(3):
            for k in range(j + 1, 4):
                if matix[k][i] > 0:
                    if matix[j][i] == 0:
                        matix[j][i] = matix[k][i]
                        matix[k][i] = 0
                    elif matix[k][i] == matix[j][i]:
                        matix[j][i] *= 2
                        score += matix[j][i]
                        matix[k][i] = 0
                    break
    addRandomNum()

def moveDown():
    global score
    for i in range(4):
        for j in range(3, 0, -1):
            for k in range(j - 1, -1, -1):
                if matix[k][i] > 0:
                    if matix[j][i] == 0:
                        matix[j][i] = matix[k][i]
                        matix[k][i] = 0
                    elif matix[j][i] == matix[k][i]:
                        matix[j][i] *= 2
                        score += matix[j][i]
                        matix[k][i] = 0
                    break
    addRandomNum()

def moveLeft():
    global score

    for i in range(4):
        for j in range(3):
            if matix[i][j] == 0 or matix[i][j] == matix[i][j+1]:
                matix[i][j] += matix[i][j+1]
                matix[i][j+1] = 0

    addRandomNum()


if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode((760, 760), 0, 32)
    pygame.display.set_caption("2048!!!")
    init_image()
    init()

    flag = True
    while True :
        m_x = m_y = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()




        screen.blit(right, (15, 340))
        screen.blit(left, (685, 340))
        screen.blit(down, (340, 685))
        screen.blit(up, (340, 13))


        screen.blit(grid_bg, (75, 75))

        temp = 125
        if 15 <= m_x <= 15 + temp and 340 <= m_y <= 340 + temp:
            moveLeft()
            if check() == False:  # 检查游戏是否GG
                print('GG')
                flag = False  # GG的话直接退出
        elif 685 <= m_x <= 685 + temp and 340 <= m_y <= 340 + temp:
            moveRight()
            if not check():  # 检查游戏是否GG
                print('GG')
                flag = False  # GG的话直接退出
        elif 340 <= m_x <= 340 + temp and 685 <= m_y <= 685 + temp:
            moveDown()
            if not check():  # 检查游戏是否GG
                print('GG')
                flag = False  # GG的话直接退出
        elif 340 <= m_x <= 340 + temp and 13 <= m_y <= 13 + temp:
            moveUp()
            if not check():  # 检查游戏是否GG
                print('GG')
                flag = False  # GG的话直接退出


        display()

        pygame.display.update()