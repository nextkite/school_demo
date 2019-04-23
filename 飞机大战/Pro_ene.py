import random


def produce_goods(goods):                           # 生成道具
    ln = random.randint(0, 550)
    if ln == 1:

        x = random.randint(30, 550)
        y = random.randint(-150, -125)

        v_x = random.randint(-10, 10) * 0.1
        v_y = random.randint(1, 5) * 0.2 + 0.5

        ln_2 = random.randint(0, 10)
        if ln_2 % 2 == 1:
            v_x = 0

        temp = (x, y, v_x, v_y)
        goods.append(temp)
    return goods


def produce_enemy_c(enemy_c, page):                     # 生成普通敌机
    ln = random.randint(0, 250)
    if ln == 1 and page != 0:
        page = page - 1
        x = random.randint(30, 550)
        y = random.randint(-150, -125)

        num = page * 3 + random.randint(1, 3)
        v_x = random.randint(-10, 10) * 0.1
        v_y = random.randint(1, 5) * 0.2 + 0.5

        ln_2 = random.randint(0, 10)
        if ln_2 % 2 == 1:
            v_x = 0

        temp = (x, y, num, page+1, v_x, v_y)
        enemy_c.append(temp)
        print(num)

    return enemy_c


def del_enemy_c(enemy_c):                                 # 删除超限敌机
    ec_len = len(enemy_c)
    for i in range(ec_len-1, -1, -1):
        x, y, num, life, v_x, v_y = enemy_c[i]
        if y > 800:
            del enemy_c[i]
    return enemy_c


def produce_enemy_cz( enemy_c, enemy_cz):                 # 生成普通敌机子弹
    ln = random.randint(0, 150)
    ec_len = len(enemy_c)
    if ln == 1 and ec_len != 0:
        ln_2 = random.randint(0, ec_len-1)
        x, y, num, life, v_x, v_y = enemy_c[ln_2]
        x = x + 54
        y = y + 75
        if num!= 17:
            temp = (x, y+30, num, v_y+0.5)
            enemy_cz.append(temp)
    return enemy_cz


def change_cz(me_z):                                      # 敌方飞机子弹的改变轨迹
    me_z_len = len(me_z)
    for i in range(me_z_len - 1, -1, -1):
        temp = me_z[i]
        del me_z[i]
        temp = (temp[0], temp[1] + temp[3], temp[2], temp[3])
        me_z.append(temp)
    return me_z


def del_cz(enemy_cz):                                     # 删除超限子弹
    ecz_len = len(enemy_cz)
    for i in range(ecz_len - 1, -1, -1):
        x, y, num, v = enemy_cz[i]
        if y > 800:
            del enemy_cz[i]
    return enemy_cz


def del_goods(goods):
    gl = len(goods)
    for i in range(gl-1, -1, -1):
        x, y, v_x, v_y = goods[i]
        if y > 1000:
            del goods[i]
    return goods



def draw_em_c(screen, em, enemy_c):                       # 画普通敌机
    for i in enemy_c:
        x, y, num, life, v_x, v_y = i
        print("num------", num-1)
        screen.blit(em[num-1], (x, y))


def draw_goods(screen, heart, goods):                     # 画道具轨迹
    for i in goods:
        screen.blit(heart, (i[0], i[1]))


def draw_em_cz(screen, emb, enemy_cz):                    # 画普通敌机的子弹
    for i in enemy_cz:
        x, y, num, v = i
        print("numzzzz", num-1)
        screen.blit(emb[num-1], (x, y))


def ch_enc(enemy_c):                                      # 画更改普通敌机轨迹
    ec_len = len(enemy_c)
    for i in range(ec_len - 1, -1, -1):
        x, y, num, life, v_x, v_y = enemy_c[i]
        if num != 17:
            del enemy_c[i]
            temp = (x+v_x, y+v_y, num, life, v_x, v_y)
            enemy_c.append(temp)
    return enemy_c


def ch_goods(goods):
    goods_len = len(goods)
    for i in range(goods_len-1, -1, -1):
        x, y, v_x, v_y = goods[i]
        del goods[i]
        temp = (x+v_x, y+v_y, v_x, v_y)
        goods.append(temp)
    return goods


def draw_boss(screen, boss, enemy_b, enemy_c):              # 画boss敌机
    x, y, v_x, v_y, life = enemy_b
    screen.blit(boss, (x, y))
    if v_x == 0 and v_y == 0:
        v_x = -1
    if y < 0:
        enemy_b = [x, y + v_y, v_x, v_y, life]
    else:
        if 50 == x:
            v_x = 1
        elif 250 == x:
            v_x = -1
        enemy_b = [x + v_x, y, v_x, 0, life]

    lk = random.randint(0, 50)
    if lk == 1:
        x = x + boss.get_width()/2
        y = y + boss.get_height()/2
        num = 16
        v_x = random.randint(-10, 10) * 0.1
        v_y = random.randint(1, 5) * 0.2 + 0.5
        enemy_c.append((x, y, num, 0, v_x, v_y))


    return enemy_b, enemy_c





if __name__ == "__main__":
    enemy_c = []
    enemy_c = produce_enemy_c(enemy_c, 5)
    print(enemy_c)