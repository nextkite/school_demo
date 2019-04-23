import datetime
from datetime import timedelta


# 画“开始游戏”
def draw_bp(screen, sta):
    screen.blit(sta, (130, 215))


# 开始按钮触发游戏事件
def butt_begin(x, y, b, page):
    temp_num = timedelta(seconds=3)
    date_temp = datetime.datetime.now()
    date_temp = date_temp + temp_num

    if page == 0 and 135 <= x <= 370 and 221 <= y <= 330 and b == 1:
        return 1, date_temp
    else:
        return page, datetime.datetime.now() - temp_num - temp_num
