import pygame
from sys import exit
from brick_breaker import ScreenSize, Racket, Ball, Brick

pygame.init()
screen_shape = ScreenSize()

screen = pygame.display.set_mode((screen_shape.screen_wight, screen_shape.screen_height))
pygame.display.set_caption("Brick breaker")
clock = pygame.time.Clock()

background = pygame.Surface((screen_shape.screen_wight, screen_shape.screen_height))
background.fill("black")

racket = pygame.sprite.GroupSingle()
racket.add(Racket())

ball = pygame.sprite.GroupSingle()
ball.add(Ball())
 
small_font = pygame.font.Font('freesansbold.ttf', 15)
large_font = pygame.font.Font('freesansbold.ttf', 25)

def display_information(lives, score, level):

    a=screen_shape.screen_wight/10
    lives_surf = small_font.render(f'Lives: {lives}',True,(255, 255, 255))
    lives_rect = lives_surf.get_rect(center = ((a*2, screen_shape.screen_height-10) ))
    screen.blit(lives_surf,lives_rect)

    score_surf = small_font.render(f'Score: {score}',True,(255, 255, 255))
    score_rect = score_surf.get_rect(center = ((a*5, screen_shape.screen_height-10) ))
    screen.blit(score_surf,score_rect)    

    level_surf = small_font.render(f'Level: {level}',True,(255, 255, 255))
    level_rect = level_surf.get_rect(center = ((a*8, screen_shape.screen_height-10) ))
    screen.blit(level_surf, level_rect)  

def racket_collision():

    if pygame.sprite.spritecollide(racket.sprite, ball, False):
        ball.sprite.y_direction = -1

def brick_collision(score):

    for brick in bricks:
        if pygame.sprite.spritecollide(brick, ball, False):
            ball.sprite.y_direction = 1
            brick.kill()
            score += 1
    return score

def lose_ball(lives):

    if ball.sprite.rect.y >= screen_shape.screen_height:
        lives -= 1
        ball.sprite.rect.x = screen_shape.screen_wight*0.5
        ball.sprite.rect.y = screen_shape.screen_height*0.25
    
    return lives

def wall_level(level):

    if level == 1:
        n_rows = 1
        n_cols = 5
        brick_width = 76
        brick_height = 10    
    elif level == 2:
        n_rows = 2
        n_cols = 10
        brick_width = 35.5
        brick_height = 10

    return {'n_rows': n_rows,
            'n_cols': n_cols,
            'brick_width': brick_width,
            'brick_height': brick_height}  
    
def make_wall(level):

    wall_metadata = wall_level(level)
    n_rows = wall_metadata['n_rows']
    n_cols = wall_metadata['n_cols']
    brick_width = wall_metadata['brick_width']
    brick_height = wall_metadata['brick_height']
    bricks = pygame.sprite.Group()
    
    for row in range(n_rows):
        for col in range(n_cols):
            brick = Brick(width = brick_width, height = brick_height)
            brick.rect.x = col * (brick.width + 5)
            brick.rect.y = row * (brick.height + 5)
            bricks.add(brick)

    return bricks

def game_over_screen(score):

    screen.blit(background, (0, 0))
    gameover_msg_surf = large_font.render(f'Game Over',True,(255, 255, 255))
    gameover_msg_rect = gameover_msg_surf.get_rect(center = ((screen_shape.screen_wight/2, screen_shape.screen_height/2 - 20 ) ))
    screen.blit(gameover_msg_surf, gameover_msg_rect)
    
    score_surf = large_font.render(f'Your score: {score}',True,(255, 255, 255))
    score_rect = score_surf.get_rect(center = ((screen_shape.screen_wight/2, screen_shape.screen_height/2 + 10) ))
    screen.blit(score_surf,score_rect)

    retry_msg_surf = small_font.render(f'Press space to play again.',True,(255, 255, 255))
    retry_msg_rect = retry_msg_surf.get_rect(center = ((screen_shape.screen_wight/2, screen_shape.screen_height/2 + 40) ))
    screen.blit(retry_msg_surf, retry_msg_rect)

def message_screen(message):

    screen.blit(background, (0, 0))
    msg_surf = large_font.render(f'{message}',True,(255, 255, 255))
    msg_rect = msg_surf.get_rect(center = ((screen_shape.screen_wight/2, screen_shape.screen_height/2 - 20 ) ))
    screen.blit(msg_surf, msg_rect)

    retry_msg_surf = small_font.render(f'Press space to play.',True,(255, 255, 255))
    retry_msg_rect = retry_msg_surf.get_rect(center = ((screen_shape.screen_wight/2, screen_shape.screen_height/2 + 40) ))
    screen.blit(retry_msg_surf, retry_msg_rect)

lives = 0
score = 0
level = 1
game_active = False
bricks = make_wall(level)

message_screen('Brick breaker')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active == False:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                if lives == 0 or level > 2:
                    lives = 3 
                    score = 0
                    level = 1
                    bricks = make_wall(level)
                else:
                   bricks = make_wall(level)
                   ball.sprite.rect.x = screen_shape.screen_wight*0.5
                   ball.sprite.rect.y = screen_shape.screen_height*0.25         

    if game_active:

        screen.blit(background, (0, 0))
        display_information(lives, score, level)
        racket_collision()
        score = brick_collision(score) 
        ball.sprite.wall_collision() #cloison with edge of screen
        lives = lose_ball(lives)

        racket.draw(screen)
        racket.update()

        ball.draw(screen)
        ball.update()
        
        bricks.draw(screen)
        bricks.update()

        if lives < 1:
            game_active = False
            game_over_screen(score)
            
        if len(bricks) == 0:
            game_active = False
            level += 1
            if level <= 2:
                message_screen('You go level up')
            else:
                message_screen('You win!')
     
    pygame.display.update()  # update screen
    clock.tick(60)
