import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_h:
        ball_speed_y *= -1

    if ball.left <= 0:
        player_score += 1
        ball_start()

    if ball.right >= screen_w:
        opponent_score += 1
        ball_start()
    
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    return 

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_h:
        player.bottom = screen_h

def opponent_animation():
    if ball.top > opponent.top:
        opponent.y += 10
    if ball.bottom < opponent.bottom:
        opponent.y -= 10

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_h:
        opponent.bottom = screen_h

def ball_start():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_w/2, screen_h/2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((-1, 1))

pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_w = 900
screen_h = 600
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption('Pong')

# Game Rectangles
ball = pygame.Rect(screen_w/2 -15, screen_h/2 -15, 30,30)
player = pygame.Rect(screen_w - 20, screen_h/2 -70, 10, 140)
opponent = pygame.Rect(10, screen_h/2  - 70, 10,140)

# Text Variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font('freesansbold.ttf', 28)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1)) 
player_speed = 0

while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN :
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 7
            if event.key == pygame.K_DOWN:
                player_speed -= 7

    ball_animation()
    player_animation()
    opponent_animation()
    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_w/2, 0), (screen_w/2, screen_h))
    
    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text,(screen_w/2 + 15, screen_h/2))

    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text,(screen_w/2 - 30, screen_h/2))

    # Updating the window
    pygame.display.flip()
    clock.tick(60)