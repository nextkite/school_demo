def draw_end(screen, end_title, level, restart, title, num, score):
    screen.blit(end_title, (160, 100))
    n = score//10 + 1
    if n >= 3:
        n = 3
    x = 80
    y = 150
    for i in range(0, n):
        screen.blit(level[i], (x, y))
        x = x + level[i].get_width()

    screen.blit(title, (190, 300))              # 画“击落”标题

    x = 260                                     # 画分数
    y = 300
    score = str(score)
    for i in range(0, len(score)):
        temp = int(score[i])
        screen.blit(num[temp], (x, y))
        x = x + num[temp].get_width() + 5

    screen.blit(restart, (170, 500))