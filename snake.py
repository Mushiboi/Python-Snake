import pygame
import time
import random

pygame.init()
pygame.display.set_caption('Slippery Snake')

white= (255,255,255)
black= (0,0,0)
red= (255,0,0)
blue = (0,0,255)
green = (50, 153, 213)
yellow = (255, 255, 102)
grey = (50, 50, 50)

dis_width = 1000
dis_height = 1000
print("width:",dis_width )
print("height",dis_height )
dis = pygame.display.set_mode((dis_width, dis_height))

game_over = False
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 30

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("helvetica", 35)
scalable_font = pygame.font.SysFont(None, int(40))

font_size_fraction = 0.02
font_size = min(dis_width, dis_height) * font_size_fraction
text_x = 150 
text_y = 150

font_style = pygame.font.SysFont(None, 30)
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def Your_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

def message(msg,color):
    mesg = scalable_font.render(msg, True, color)
    dis.blit(mesg, [text_x, text_y])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0
    snake_list = []
    snake_length = 1

    foodx = random.randint(0, (dis_width - snake_block) // snake_block) * snake_block
    foody = random.randint(0, (dis_width - snake_block) // snake_block) * snake_block

    while not game_over:
        while game_close == True:
            dis.fill(grey)
            message("You Lost! Press Q to Quit or Space to Play Again!", red)
            Your_score(snake_length -1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(grey)
        pygame.draw.rect(dis, white, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        Your_score(snake_length -1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = random.randint(0, (dis_width - snake_block) // snake_block) * snake_block
            foody = random.randint(0, (dis_width - snake_block) // snake_block) * snake_block
            snake_length += 1
 
        clock.tick(snake_speed)
    

    pygame.quit()
    quit()

gameLoop()
