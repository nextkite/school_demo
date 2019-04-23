def draw_bg(screen, bg, flag_bg):                  # 画背景
    screen.blit(bg[flag_bg], (0, 0))
    screen.blit(bg[flag_bg], (300, 0))
    screen.blit(bg[flag_bg], (0, 300))
    screen.blit(bg[flag_bg], (300, 300))
    screen.blit(bg[flag_bg], (0, 600))
    screen.blit(bg[flag_bg], (300, 600))


def draw_me_life(screen, life, num):               # 画我方敌机生命值
    x = 20
    y = 640
    for i in range(0, num):
        screen.blit(life, (x, y))
        x = x + life.get_width()+5


def draw_pause(screen, pause):                     # 画暂停按钮
    screen.blit(pause, (200, 250))


def draw_me_sound(screen, sc, so, sound_flag):     # 画暂停声音按钮
    if sound_flag == 0:
        screen.blit(so, (415, 635))
    else:
        screen.blit(sc, (415, 635))


def draw_title(screen, title):                     # 画“击落”标题
    screen.blit(title, (0, 0))


def draw_score(screen, num, score):                # 画分数
    x = 70
    y = 0
    score = str(score)
    for i in range(0, len(score)):
        temp = int(score[i])
        screen.blit(num[temp], (x, y))
        x = x + num[temp].get_width() + 5





