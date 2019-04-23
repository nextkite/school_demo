import pygame
pygame.init()
shot = pygame.mixer.Sound("./sound/shot.ogg")       # 子弹射击
back_sound = pygame.mixer.Sound("./sound/win.ogg")  # 背景音乐
game_over = pygame.mixer.Sound("./sound/lose.ogg")  # 游戏结束
boss_show = pygame.mixer.Sound("./sound/boss.ogg")  # Boss 出现
goods_sound = pygame.mixer.Sound("./sound/shengxing.ogg")   # 加补给
count_down = pygame.mixer.Sound("./sound/jingbao.ogg")      # 倒计时
enemy_dead = pygame.mixer.Sound("./sound/Boom.ogg")         # 敌机损坏

# 子弹音效  shot.ogg
def Bullet_Sound(sound_flag):
    if sound_flag == 0:
        shot.play()
        shot.set_volume(0.8)

# 背景音乐控制 sound_flag 0 开启音乐 1 关闭音乐
# def Black_Sound(sound_flag):
#     if sound_flag == 0:
#         # back_sound.play(-1)
#         # back_sound.set_volume(0.3)
#     else:
#         back_sound.stop()

# 游戏结束
def Game_Over(sound_flag):
    if sound_flag == 0:
        game_over.play()

# Boss 出现
def Boss_Show(sound_flag):
    if sound_flag == 0:
        boss_show.play()

# 加道具
def Goods_Sound(sound_flag):
    if sound_flag == 0:
        goods_sound.play()

# 进入游戏倒计时 发出三次声响
def Count_Down(sound_flag):
    if sound_flag == 0:
        count_down.play(2)

# 敌机损坏声音
def Enemy_Dead(sound_flag):
    if sound_flag == 0:
        enemy_dead.play()

