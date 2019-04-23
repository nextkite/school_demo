import pygame
import datetime
import random
from sys import exit
from Prepare_Page import prepare_value
from End_Page import *
from Background_Page import *
from Begin_Page import *
from Pass_1 import draw_ps
from Me_page import *
from Pro_ene import *
from Accident_Page import *
from Sound import *

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((500, 700), 0, 32)
    pygame.display.set_caption("Fly2.0!!!")

    # 参数准备
    bg, flag_bg, sta, ps, me_plane, life, pause, sc, so, meb, title, em, emb, num, exp, end_title, level, restart, heart, boss = prepare_value()

    page = 0                             # 页面码
    time_link = datetime.datetime.now()  # 获取系统当前时间
    score = 0                            # 分数
    life_num = 3                         # 生命剩余
    pause_temp = 0                       # 暂停替换页
    sound_flag = 0                       # 声音开关
    enemy_c = []                         # 普通敌机列表
    enemy_b = [150, -100, 0, 1, 50]      # boss敌机列表
    enemy_cz = []                        # 敌机子弹列表
    goods = []                           # 道具列表
    explode = []                         # 爆炸列表
    me_z = []                            # 我方子弹
    m_x = m_y = 0                        # 鼠标初始坐标
    # Black_Sound(sound_flag)

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
                    me_z.append((x, y-45, score, 0.8+0.6*page))
                    Bullet_Sound(sound_flag)  # 点击鼠标

                if 1 <= page <= 5 and b == 3:                      # 暂停按钮的触发
                    pause_temp = page
                    page = 7
                elif page == 7 and b == 3:
                    page = pause_temp

                if 420 < x < 640 and 640 < y < 670 and sound_flag == 0:  # 声音按钮的开关


                    sound_flag = 1
                    # Black_Sound(sound_flag)
                elif 420 < x < 640 and 640 < y < 670 and sound_flag == 1:

                    sound_flag = 0
                    # Black_Sound(sound_flag)

                if page == 6 and 175 < x < 175 + restart.get_width() and 500 < y < 500 + restart.get_height():
                    page = 0  # 页面码
                    time_link = datetime.datetime.now()  # 获取系统当前时间
                    score = 0  # 分数
                    life_num = 3  # 生命剩余
                    pause_temp = 0  # 暂停替换页
                    sound_flag = 0  # 声音开关
                    enemy_c = []  # 普通敌机列表
                    enemy_b = [150, -100, 0, 1, 50]  # boss敌机列表
                    enemy_cz = []  # 敌机子弹列表
                    explode = []  # 爆炸列表
                    me_z = []  # 我方子弹
                    goods = []  # 道具列表
                    m_x = m_y = 0  # 鼠标初始坐标

        # 以下是画图部分
        draw_bg(screen, bg, flag_bg)               # 画背景
        draw_me_sound(screen, sc, so, sound_flag)  # 画声音开关

        if page == 0:                       # 画开始页面
            draw_bp(screen, sta)
        elif page == 1:                     # 画关卡1
            if time_link > time_now:
                draw_ps(screen, ps, page)                  # 画关卡1名称

            if life_num > 0:
                draw_me(screen, me_plane, score, m_x, m_y) # 画我方飞机，分数，坐标
            draw_my_buttle(screen, meb, score, me_z)       # 画我方飞机子弹
            draw_title(screen, title)                      # 画“击落”标题
            draw_score(screen, num, score)                 # 画分数
            draw_me_life(screen, life, life_num)           # 画生命数
            draw_goods(screen, heart, goods)               # 画道具

            explode = draw_exp(screen, exp, explode)       # 画爆炸
            draw_em_c(screen, em, enemy_c)                 # 画普通敌机
            draw_em_cz(screen, emb, enemy_cz)              # 画敌机子弹
                                                           # 画boss敌机
                                                           # 画boss敌机子弹
            if score > 10:
                page = 2

        elif page == 2:                     # 画关卡1
            if time_link > time_now:
                draw_ps(screen, ps, page)                  # 画关卡1名称

            if life_num > 0:
                draw_me(screen, me_plane, score, m_x, m_y) # 画我方飞机，分数，坐标
            draw_my_buttle(screen, meb, score, me_z)       # 画我方飞机子弹
            draw_title(screen, title)                      # 画“击落”标题
            draw_score(screen, num, score)                 # 画分数
            draw_me_life(screen, life, life_num)           # 画生命数
            draw_goods(screen, heart, goods)               # 画道具

            explode = draw_exp(screen, exp, explode)       # 画爆炸
            draw_em_c(screen, em, enemy_c)                 # 画普通敌机
            draw_em_cz(screen, emb, enemy_cz)              # 画敌机子弹
                                                           # 画boss敌机
                                                           # 画boss敌机子弹
            if score > 20:
                page = 3

        elif page == 3:                                    # 画关卡3
            if time_link > time_now:
                draw_ps(screen, ps, page)                  # 画关卡3名称

            if life_num > 0:
                draw_me(screen, me_plane, score, m_x, m_y) # 画我方飞机，分数，坐标
            draw_my_buttle(screen, meb, score, me_z)       # 画我方飞机子弹
            draw_title(screen, title)                      # 画“击落”标题
            draw_score(screen, num, score)                 # 画分数
            draw_me_life(screen, life, life_num)           # 画生命数
            draw_goods(screen, heart, goods)               # 画道具

            explode = draw_exp(screen, exp, explode)       # 画爆炸
            draw_em_c(screen, em, enemy_c)                 # 画普通敌机
            draw_em_cz(screen, emb, enemy_cz)              # 画敌机子弹
                                                           # 画boss敌机
                                                           # 画boss敌机子弹
            if score > 30:
                page = 4

        elif page == 4:  # 画关卡3
            if time_link > time_now:
                draw_ps(screen, ps, page)  # 画关卡3名称

            if life_num > 0:
                draw_me(screen, me_plane, score, m_x, m_y)  # 画我方飞机，分数，坐标
            draw_my_buttle(screen, meb, score, me_z)  # 画我方飞机子弹
            draw_title(screen, title)  # 画“击落”标题
            draw_score(screen, num, score)  # 画分数
            draw_me_life(screen, life, life_num)  # 画生命数
            draw_goods(screen, heart, goods)  # 画道具

            explode = draw_exp(screen, exp, explode)  # 画爆炸
            draw_em_c(screen, em, enemy_c)  # 画普通敌机
            draw_em_cz(screen, emb, enemy_cz)  # 画敌机子弹
            # 画boss敌机
            # 画boss敌机子弹
            if score > 40:
                page = 5

        elif page == 5:  # 画关卡3
            if time_link > time_now:
                draw_ps(screen, ps, page)  # 画关卡3名称

            if life_num > 0:
                draw_me(screen, me_plane, score, m_x, m_y)  # 画我方飞机，分数，坐标
            draw_my_buttle(screen, meb, score, me_z)  # 画我方飞机子弹
            draw_title(screen, title)  # 画“击落”标题
            draw_score(screen, num, score)  # 画分数
            draw_me_life(screen, life, life_num)  # 画生命数
            draw_goods(screen, heart, goods)  # 画道具

            explode = draw_exp(screen, exp, explode)  # 画爆炸
            draw_em_c(screen, em, enemy_c)  # 画普通敌机
            draw_em_cz(screen, emb, enemy_cz)  # 画敌机子弹
            # 画boss敌机
            # 画boss敌机子弹
            if score > 50 and enemy_b[4] > 0:
                enemy_b, enemy_c = draw_boss(screen, boss, enemy_b, enemy_c)
                me_z, enemy_b, explode = me_z_and_b(me_z, enemy_b, explode)
                explode = draw_exp(screen, exp, explode)  # 画爆炸
            if enemy_b[4] == 0:
                page = 6

        elif page == 6:
            draw_end(screen, end_title, level, restart, title, num, score)

        elif page == 7:                      # 画暂停按钮
            draw_me(screen, me_plane, score, m_x, m_y)  # 画我方飞机，分数，坐标
            draw_my_buttle(screen, meb, score, me_z)  # 画我方飞机子弹
            draw_title(screen, title)  # 画“击落”标题
            draw_score(screen, num, score)  # 画分数
            draw_me_life(screen, life, life_num)  # 画生命数
            draw_goods(screen, heart, goods)  # 画道具

            explode = draw_exp(screen, exp, explode)  # 画爆炸
            draw_em_c(screen, em, enemy_c)  # 画普通敌机
            draw_em_cz(screen, emb, enemy_cz)  # 画敌机子弹

            draw_pause(screen, pause)                      # 绘画暂停按钮





        pygame.display.update()              # 更新画板

        # 事件处理,只有在关卡1~5才会发生这些事件
        if 1 <= page <= 5:


            goods = produce_goods(goods)                                    # 生成道具

            goods = ch_goods(goods)                                         # 道具轨迹更改

            goods = del_goods(goods)                                        # 删除超限道具

            enemy_c = produce_enemy_c(enemy_c, page)                        # 生产普通敌机

            enemy_c = del_enemy_c(enemy_c)                                  # 消除普通敌机

            enemy_c = ch_enc(enemy_c)                                       # 普通敌机轨迹更改

            enemy_cz = produce_enemy_cz(enemy_c, enemy_cz)                  # 普通敌机产生的子弹

            enemy_cz = change_cz(enemy_cz)                                  # 普通敌方子弹更改

            enemy_cz = del_cz(enemy_cz)                                     # 普通敌机子弹删除

            me_z = change(me_z)                                             # 我方子弹轨迹更改

            me_z = del_me_z(me_z)                                           # 我方子弹删除

                                                                            # 我方子弹与敌机相撞
            me_z, enemy_c, explode, score = me_z_and_enemy_c(screen, meb, em, me_z, enemy_c, explode, score, sound_flag)

                                                                            # 敌方子弹与我机相撞
            enemy_cz, explode, life_num = me_and_enemy_cz(m_x, m_y, explode, emb, enemy_cz, life_num, sound_flag)

                                                                            # 敌方飞机与我机相撞
            enemy_c, explode, life_num = me_and_enemy_c(m_x, m_y, explode, em, enemy_c, life_num, sound_flag)

                                                                            # 道具与我机相撞
            goods, life_num = me_and_goods(m_x, m_y, heart, goods, life_num, sound_flag)




        if life_num == 0:
            page = 6
            Game_Over(sound_flag)



















