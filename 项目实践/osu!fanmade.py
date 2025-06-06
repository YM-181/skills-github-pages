import sys
import os
from re import fullmatch

import pygame
import time
import random
import keyboard

# ===初始化===
pygame.init()
pygame.mixer.init()  # 初始化音频系统
sound1=pygame.mixer.Sound('Sound1.mp3')
sound2=pygame.mixer.Sound('Hit_Sound.mp3')
# === 创建游戏窗口（1280*720像素）===
screen_width,screen_height = 1280,720
screen = pygame.display.set_mode((screen_width, screen_height))  # [1,5](@ref)
pygame.display.set_caption("osu!FanMade")
background = pygame.image.load("background.jpg")  # 替换为你的图片路径
    # 可选：调整图片大小以匹配窗口
background = pygame.transform.scale(background, (screen_width, screen_height))
# 创建时间对象
clock = pygame.time.Clock()
fps = 144


# === circles: ===
class HitCircle:
    #初始化参数
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.radius = 40
        self.active = True
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = 2000
    # === 初始化外形 ===
    def draw(self,screen):
        if self.active:
            #外圆
            pygame.draw.circle(screen,(255,100,100),(self.x,self.y),self.radius,3)
            #内圆
            pygame.draw.circle(screen,(255,50,50),(self.x,self.y),self.radius-15)
    # === 打击判定 ===
    def update(self):
        if pygame.time.get_ticks()-self.spawn_time>self.lifetime:
            self.active = False
            return "MISS"
        return None
    
# === UI初始化&游戏变量初始化 ===

circles = []  # 存储所有音符
spawn_interval = 1500  # 音符生成间隔(毫秒)
last_spawn = 0  # 上次生成时间
score = 0
combo = 0
max_combo_value = 0
max_combo_value_1 = 0
font = pygame.font.SysFont(None, 36)  # 计分字体
    
running = True
#游戏循环
start_time=time.perf_counter()
end_time=start_time+20
while running:
    now_time=time.perf_counter()
    left_time=end_time-now_time         
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
        
# === 着色背景颜色 ===
    #screen.fill((217,179,48))
    screen.blit(background, (0, 0))
    

    
#-------------------------主程序:-------------------------------------
# === 音符生成 ===
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn > spawn_interval:
    # 随机生成位置（避开边缘）
        new_x = random.randint(100, screen_width-100)
        new_y = random.randint(100, screen_height-100)
        circles.append(HitCircle(new_x, new_y))
        last_spawn = current_time
# === 音符更新与消失检测 ===
    for circle in circles[:]:  # 使用切片创建副本避免修改问题
        result = circle.update()
        if result == "MISS":
            circles.remove(circle)
            combo = 0  # 连击中断
            if max_combo_value_1 < max_combo_value:
                max_combo_value_1 = max_combo_value
                max_combo_value = 0

# === 鼠标点击检测 ===
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for circle in circles:
            if circle.active:
                distance = ((mouse_x - circle.x)**2 + (mouse_y - circle.y)**2)**0.5
            if distance <= circle.radius:
                ran=random.randint(1, 2)
                if ran==1:
                    sound1.play()
                else:
                    sound2.play()
                circle.active = False
                # 计算精准度（时间差越小分越高）
                time_diff = pygame.time.get_ticks() - circle.spawn_time
                accuracy = max(0, 1 - abs(time_diff - 1000)/1000)  # 理想点击时间1000ms                
                score += int(100 * accuracy * (1 + combo/10))  # 连击加成[11](@ref)
                combo += 1
                max_combo_value += 1
                circles.remove(circle)
# === 绘制所有音符 ===
    for circle in circles:
        circle.draw(screen)
# === 显示分数和连击 ===
    left_time_text= font.render(f"countdown: {left_time:.0f}", True, (0, 0, 0))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    combo_text = font.render(f"Combo: {combo}", True, (0, 255, 255))
    screen.blit(left_time_text, (20, 100))
    screen.blit(score_text, (20, 20))
    screen.blit(combo_text, (20, 60))

# === 更新画面 ===
    pygame.display.flip()
# === 控制帧率 === 
    clock.tick(fps)
# === 关闭游戏界面 ===
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if left_time<=0:
            screen.fill((0,0,0))
            final_score = font.render(f"Final score: {score}", True, (255, 255, 255))
            max_combo = font.render(f"Max combo: {max_combo_value_1}", True, (0, 255, 255))
            screen.blit(final_score, (screen_width // 2 - 100, screen_height // 2 - 50))
            screen.blit(max_combo, (screen_width // 2 - 100, screen_height // 2))
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.quit()
            sys.exit()