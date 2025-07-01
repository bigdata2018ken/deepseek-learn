import pygame
import time
import random

# 初始化 Pygame
pygame.init()

# 定义颜色
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 设置游戏窗口尺寸
dis_width = 800
dis_height = 600

# 创建游戏窗口
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('贪吃蛇 by Gemini')

# 设置游戏时钟
clock = pygame.time.Clock()

# 设置蛇块的大小和速度
snake_block = 10
snake_speed = 15

# ==================== 修改部分 ====================
# 设置字体样式 - 使用字体文件以确保跨平台兼容性
# 请确保有一个名为 "simhei.ttf" 的字体文件与此脚本在同一目录下
# 您也可以换成其他 .ttf 格式的中文字体文件
try:
    font_style = pygame.font.Font("simhei.ttf", 25)
    score_font = pygame.font.Font("simhei.ttf", 35)
except FileNotFoundError:
    print("字体文件'simhei.ttf'未找到，将使用系统默认字体，中文可能无法显示。")
    # 如果找不到字体文件，回退到系统字体
    font_style = pygame.font.SysFont("Microsoft YaHei", 25)  # 尝试使用Windows的雅黑
    score_font = pygame.font.SysFont("Microsoft YaHei", 35)


# ================================================


def our_snake(snake_block, snake_list):
    """绘制蛇的函数"""
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    """在屏幕上显示消息的函数"""
    mesg = font_style.render(msg, True, color)
    # 居中显示消息
    mesg_rect = mesg.get_rect(center=(dis_width / 2, dis_height / 3))
    dis.blit(mesg, mesg_rect)


def show_score(score):
    """显示分数的函数"""
    value = score_font.render("分数: " + str(score), True, yellow)
    dis.blit(value, [10, 10])  # 显示在左上角


def gameLoop():
    """游戏主循环"""
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("你输了！按 Q 退出或按 C 重新开始", red)
            show_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        show_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


# 启动游戏
gameLoop()