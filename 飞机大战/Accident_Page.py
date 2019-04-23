import random
from Sound import *

def me_z_and_enemy_c(screen, meb, em, me_z, enemy_c, explode, score, sound_flag):
    len_m = len(me_z)

    for i in range(len_m-1, -1, -1):
        m_x = me_z[i][0]
        m_y = me_z[i][1]
        m_num = me_z[i][2] // 10

        if m_num >= 4:
            m_num = 3

        m_x = m_x - meb[m_num].get_width() / 2
        m_y = m_y - meb[m_num].get_height() / 2

        flag = 1
        len_e = len(enemy_c)
        for j in range(len_e-1, -1, -1):
            e_x = enemy_c[j][0]
            e_y = enemy_c[j][1]
            e_num = enemy_c[j][2]
            e_num = e_num - 1

            if e_x <= m_x <= e_x + em[e_num].get_width()-20 and (abs(e_y - m_y) < 50) and e_num < 15:
                flag = 0
                del enemy_c[j]
                explode.append([e_x, e_y, 0, 50])
                break
            if e_x <= m_x <= e_x + em[e_num].get_width() and (abs(e_y - m_y) < 50) and e_num == 15:

                flag = 0
                Enemy_Dead(sound_flag)

                del enemy_c[j]


                explode.append([e_x-40, e_y-40, 0, 50])
                temp = [e_x-30, e_y-30, 17, 0, 0, 0]
                enemy_c.append(temp)
                break

        if flag == 0:
            score = score + 1
            del me_z[i]

    return me_z, enemy_c, explode, score


def draw_exp(screen, exp, explode):                                             # 画爆炸场面
    ll = len(explode)
    for i in range(ll-1, -1, -1):
        screen.blit(exp[explode[i][2]//25], (explode[i][0], explode[i][1]))
        explode[i][2] = explode[i][2] + 1
        if explode[i][2] >= explode[i][3]:
            del explode[i]
    return explode


def me_and_enemy_cz(m_x, m_y, explode, emb, enemy_cz, life, sound_flag):                    # 我机与敌机子弹相撞
    ll = len(enemy_cz)

    for i in range(ll-1, -1, -1):
        e_x = enemy_cz[i][0]
        e_y = enemy_cz[i][1]
        if m_x-40 <= e_x <= m_x+40 and (abs(m_y-e_y)<50) and life != 0:
            explode.append([m_x-75, m_y-80, 0, 30])
            Enemy_Dead(sound_flag)
            del enemy_cz[i]
            life = life - 1

    return enemy_cz, explode, life


def me_and_enemy_c(m_x, m_y, explode, em, enemy_c, life_num, sound_flag):                   # 我机与敌机相撞
    ll = len(enemy_c)

    for i in range(ll-1, -1, -1):
        e_x = enemy_c[i][0]
        e_y = enemy_c[i][1]
        e_num = enemy_c[i][2]
        e_x1 = e_x + em[e_num-1].get_width()
        e_y1 = e_y + em[e_num-1].get_height()

        if e_x-23 <= m_x <= e_x1+23 and -80 < m_y - e_y1 < -20 and life_num != 0:
            explode.append([m_x-75, m_y-80, 0, 30])
            explode.append([e_x, e_y, 0, 50])
            if e_num != 17:
                Enemy_Dead(sound_flag)

                del enemy_c[i]
            life_num = life_num - 1

    return enemy_c, explode, life_num


def me_and_goods(m_x, m_y, heart, goods, life_num, sound_flag):                              # 道具与我机相撞
    ll = len(goods)
    for i in range(ll-1, -1, -1):
        e_x = goods[i][0]
        e_y = goods[i][1]

        e_x1 = e_x + heart.get_width()
        e_y1 = e_y + heart.get_height()

        if e_x-23 <= m_x <= e_x1+23 and -80 < m_y - e_y1 < -20 and life_num != 0:
            Goods_Sound(sound_flag) # 道具声音
            del goods[i]
            life_num = life_num + 1
            if life_num > 6:
                life_num = 6

    return goods, life_num


def  me_z_and_b(me_z, enemy_b, explode):
    lz = len(me_z)
    print("Lz------------------------", lz)
    for i in range(lz-1, -1, -1):
        x = me_z[i][0] + 10
        y = me_z[i][1] - 20

        b_x = enemy_b[0]
        print("Bx___x",x, b_x)
        b_y = enemy_b[1]

        if b_x + 30 < x < b_x + 170 and abs(b_y - y) < 50:
            print("     =============    ")
            enemy_b[4] = enemy_b[4] - 1
            explode.append([x, y, 0, 30])
            del me_z[i]
        if enemy_b[4] == 0:
            explode.append([enemy_b[0]+100, enemy_b[1]+125, 0, 120])
    return me_z, enemy_b, explode









