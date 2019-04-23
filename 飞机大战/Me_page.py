
def draw_me(screen, me, score, m_x, m_y):                 # 画我方飞机
    if score < 10:
        me = me[0]
    elif score < 20:
        me = me[1]
    elif score < 30:
        me = me[2]
    else:
        me = me[3]

    m_x = m_x - me.get_width() / 2
    m_y = m_y - me.get_height() / 2

    screen.blit(me, (m_x, m_y))


def draw_my_buttle(screen, meb, score, me_z):             # 画我方飞机子弹
    if score < 10:
        meb = meb[0]
    elif score < 20:
        meb = meb[1]
    elif score < 30:
        meb = meb[2]
    else:
        meb = meb[3]

    me_z_len = len(me_z)
    for i in range(0, me_z_len):
        x = me_z[i][0]
        y = me_z[i][1]
        x = x - meb.get_width() / 2
        y = y - meb.get_height() / 2

        screen.blit(meb, (x, y))


def change(me_z):                                 # 我方飞机子弹的改变轨迹
    me_z_len = len(me_z)
    for i in range(me_z_len - 1, -1, -1):
        temp = me_z[i]
        del me_z[i]
        temp = (temp[0], temp[1] - temp[3], temp[2], temp[3])
        me_z.append(temp)
    return me_z


def del_me_z(me_z):                               # 删除超限子弹
    me_z_len = len(me_z)
    for i in range(me_z_len - 1, -1, -1):
        temp = me_z[i]
        if temp[1] < -50:
            del me_z[i]
    return me_z


