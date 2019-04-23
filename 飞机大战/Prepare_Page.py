# 准备页面，主要负责图片的批量加载，然后传给主代码页
import pygame
import random


def prepare_value():

    bg = ["./background/background_1.png",              # 背景图片的批量加载
          "./background/background_2.png",
          "./background/background_3.png",
          "./background/background_1.png"]
    for i in range(0, 4):
        bg[i] = pygame.image.load(bg[i])
    flag_bg = int(random.randint(0, 3))                 # 随机选择一个背景页面

    sta = pygame.image.load("./button/Start.png")       # “开始游戏”按钮的加载

    ps = ["./pass/ps_1.png",                            # 关卡标题图片的批量加载
          "./pass/ps_2.png",
          "./pass/ps_3.png",
          "./pass/ps_4.png",
          "./pass/ps_5.png"]
    for i in range(0, 5):
        ps[i] = pygame.image.load(ps[i])

    me_plane = ["./me_plane/me_1.png",                  # 我方不同型态飞机图片的批量加载
                "./me_plane/me_2.png",
                "./me_plane/me_3.png",
                "./me_plane/me_4.png"]
    for i in range(0, 4):
        me_plane[i] = pygame.image.load(me_plane[i])

    life = "./background/life.png"                      # 代表生命值的蓝色小飞机的图片
    life = pygame.image.load(life)

    pause = "./background/pause.png"                    # 暂停按钮图片
    pause = pygame.image.load(pause)

    sc = "./background/SoundClose.png"                  # 声音开关的图片
    so = "./background/SoundOpen.png"
    sc = pygame.image.load(sc)
    so = pygame.image.load(so)

    meb = ["./me_plane/meb_1.png",                      # 我方不同形态子弹图片的批量加载
           "./me_plane/meb_2.png",
           "./me_plane/meb_3.png",
           "./me_plane/meb_4.png"]
    for i in range(0, 4):
        meb[i] = pygame.image.load(meb[i])

    title = "./background/title.png"                    # “击落”标题图片
    title = pygame.image.load(title)

    em = ["./enemy_plane/em_1.png",                     # 普通敌机图片的批量加载
          "./enemy_plane/em_2.png",
          "./enemy_plane/em_3.png",
          "./enemy_plane/em_4.png",
          "./enemy_plane/em_5.png",
          "./enemy_plane/em_6.png",
          "./enemy_plane/em_7.png",
          "./enemy_plane/em_8.png",
          "./enemy_plane/em_9.png",
          "./enemy_plane/em_10.png",
          "./enemy_plane/em_11.png",
          "./enemy_plane/em_12.png",
          "./enemy_plane/em_13.png",
          "./enemy_plane/em_14.png",
          "./enemy_plane/em_15.png",
          "./enemy_plane/emb_16.png",
          "./enemy_plane/emb_17.png"]

    for i in range(0, 17):
        em[i] = pygame.image.load(em[i])

    emb = ["./enemy_plane/emb_1.png",                     # 普通敌机子弹图片的批量加载
           "./enemy_plane/emb_2.png",
           "./enemy_plane/emb_3.png",
           "./enemy_plane/emb_4.png",
           "./enemy_plane/emb_5.png",
           "./enemy_plane/emb_6.png",
           "./enemy_plane/emb_7.png",
           "./enemy_plane/emb_8.png",
           "./enemy_plane/emb_9.png",
           "./enemy_plane/emb_10.png",
           "./enemy_plane/emb_11.png",
           "./enemy_plane/emb_12.png",
           "./enemy_plane/emb_13.png",
           "./enemy_plane/emb_14.png",
           "./enemy_plane/emb_15.png",
           "./enemy_plane/emb_16.png",
           "./enemy_plane/emb_17.png"]

    for i in range(0, 17):
        emb[i] = pygame.image.load(emb[i])

    num = ["./Number/num_0.png",                          # 数字显示加载
           "./Number/num_1.png",
           "./Number/num_2.png",
           "./Number/num_3.png",
           "./Number/num_4.png",
           "./Number/num_5.png",
           "./Number/num_6.png",
           "./Number/num_7.png",
           "./Number/num_8.png",
           "./Number/num_9.png"]

    for i in range(0, 10):
        num[i] = pygame.image.load(num[i])

    explode = ["./explode/explode1.png",
               "./explode/explode2.png",
               "./explode/explode3.png",
               "./explode/explode4.png",
               "./explode/explode5.png"]

    for i in range(0, 5):
        explode[i] = pygame.image.load(explode[i])

    end_title = pygame.image.load("./end/End_title.png")   # 结束标题
    L_1 = pygame.image.load("./end/L_1.png")               # 等级图片
    L_2 = pygame.image.load("./end/L_2.png")
    L_3 = pygame.image.load("./end/L_3.png")
    level = [L_1, L_2, L_3]
    restart = pygame.image.load("./end/Restart.png")       # 重新开始图片

    heart = pygame.image.load("./background/heart.png")    # 心形道具

    boss = pygame.image.load("./enemy_plane/boss_5.png")   # boss飞机






    return bg, flag_bg, sta, ps, me_plane, life, pause, sc, so, meb, title, em, emb, num, explode, end_title, level, restart, heart, boss


