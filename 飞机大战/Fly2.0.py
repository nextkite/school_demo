import pygame
import datetime
import random
from sys import exit
from Prepare_Page import prepare_value
from Background_Page import *
from Begin_Page import *
from Pass_1 import draw_ps
from Me_page import *
from Pro_ene import *

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((500, 700), 0, 32)
    pygame.display.set_caption("Fly2.0!!!")

    # 参数准备
    bg, flag_bg, sta, ps, me_plane, life, pause, sc, so, meb, title, em, emb = prepare_value()

    page = 0                             # 页面码
    time_link = datetime.datetime.now()  # 获取系统当前时间
    score = 0                            # 分数
    life_num = 3                         # 生命剩余
    pause_temp = 0                       # 暂停替换页
    sound_flag = 0                       # 声音开关
    enemy_c = []                         # 普通敌机列表
    enemy_b = []                         # boss敌机列表
    enemy_cz = []                        # 敌机子弹列表
    me_z = []                            # 我方子弹
    m_x = m_y = 0                        # 鼠标初始坐标

    while True:
        time_now = datetime.datetime.now()       # 获取系统时间
        if 1 <= page <= 5:
            m_x, m_y = pygame.mouse.get_pos()    # 获取鼠标位置

        for event in pygame.event.get():
            if event.type == pygame.QUIT:        # 退出游戏
                exit()

            elif event.type == pygame.MOUSEBUTTONUP:     # 鼠标点击事件处理
                x, y = event.pos
                b = int(event.button)

                page, time_link = butt_begin(x, y, b, page)        # 进入游戏按钮

                if 1 <= page <= 5:                                 # 发射子弹事件
                    me_z.append((x, y-45, 0, 0.8+0.6*page))

                if 1 <= page <= 5 and b == 3:                      # 暂停按钮的触发
                    pause_temp = page
                    page = 7
                elif page == 7 and b == 3:
                    page = pause_temp

                if 420 < x < 640 and 640 < y < 670 and sound_flag == 0:  # 声音按钮的开关
                    sound_flag = 1
                elif 420 < x < 640 and 640 < y < 670 and sound_flag == 1:
                    sound_flag = 0

        # 以下是画图部分
        draw_bg(screen, bg, flag_bg)               # 画背景
        draw_me_sound(screen, sc, so, sound_flag)  # 画声音开关

        if page == 0:                       # 画开始页面
            draw_bp(screen, sta)
        elif page == 1:                     # 画关卡1
            if time_link > time_now:
                draw_ps(screen, ps, page)                  # 画关卡1名称

            draw_me(screen, me_plane, score, m_x, m_y)     # 画我方飞机，分数，坐标
            draw_my_buttle(screen, meb, score, me_z)       # 画我方飞机子弹
            draw_title(screen, title)                      # 画“击落”标题
            draw_me_life(screen, life, life_num)           # 画生命数

            draw_em_c(screen, em, enemy_c)                 # 画普通敌机
            draw_em_cz(screen, emb, enemy_cz)              # 画敌机子弹
                                                           # 画boss敌机
                                                           # 画boss敌机子弹

        elif page == 7:                      # 画暂停按钮
            draw_pause(screen, pause)                      # 绘画暂停按钮

        pygame.display.update()              # 更新画板

        # 事件处理,只有在关卡1~5才会发生这些事件
        if 1 <= page <= 5:
            enemy_c = produce_enemy_c(enemy_c, page)        # 生产普通敌机

            enemy_c = del_enemy_c(enemy_c)                  # 消除普通敌机

            enemy_c = ch_enc(enemy_c)                       # 普通敌机轨迹更改

            enemy_cz = produce_enemy_cz(enemy_c, enemy_cz)  # 普通敌机产生的子弹

            me_z = change(me_z)                             # 我方子弹轨迹更改








