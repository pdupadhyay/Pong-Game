import pygame, time, sys, random

pygame.init()
clock = pygame.time.Clock()
screen_height = 710
screen_width = 1350
screen1 = pygame.display.set_mode((screen_width,screen_height))
screen2 = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")


player2_speed = 0
player1_speed = 0
opponent_speed = 10
ball_speed_x = 4*random.choice((-1,1))
ball_speed_y = 4*random.choice((-1,1))
player2_score = 0
player1_score = 0
opponent_score = 0


def game():

    global player2_speed, player1_speed, opponent_speed, ball_speed_x , ball_speed_y , player2_score, player1_score, opponent_score

    def player2_mov():
        player2.y += player2_speed
        if player2.top <= 0:
            player2.top = 0

        if player2.bottom >= screen_height:
            player2.bottom = screen_height


    def player1_mov():
        player1.y += player1_speed
        if player1.top <= 0:
            player1.top = 0

        if player1.bottom >= screen_height:
            player1.bottom = screen_height


    def ball_mov():
        global ball_speed_x, ball_speed_y, player2_score, player1_score, opponent_score
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.top <= 0:
            ball_speed_y *= -1

        if ball.bottom >= screen_height:
            ball_speed_y *= -1
        if mouse[0] < screen_width/2:
            if ball.colliderect(player2) or ball.colliderect(opponent):
                ball_speed_x *= -1
        elif mouse[0] > screen_width/2:
            if ball.colliderect(player2) or ball. colliderect(player1):
                ball_speed_x *= -1

        if ball.left <= 0:
            if mouse[0] > screen_width/2:
                player1_score += 1
            elif mouse[0] < screen_width/2:
                opponent_score += 1
            ball_restart()

        if ball.right >= screen_width:
            player2_score += 1
            ball_restart()


    def ball_restart():
        global ball_speed_x,ball_speed_y
        ball.center = (screen_width/2, screen_height/2)
        ball_speed_x = 4*random.choice((-1,1))
        ball_speed_y = 4*random.choice((-1,1))

    def opponent_mov():
        if opponent.top <= 0:
            opponent.top = 0

        if opponent.bottom >= screen_height:
            opponent.bottom = screen_height

        if ball.y < opponent.top:
            opponent.y -= opponent_speed

        if ball.y > opponent.top:
            opponent.y += opponent_speed

    game_font = pygame.font.SysFont("Times New Roman", 48)
    ball = pygame.Rect(screen_width/2, screen_height/2,20,20)
    player2 = pygame.Rect(10, screen_height/2, 10, 100)
    if mouse[0] > screen_width/2:
        player1 = pygame.Rect(screen_width-20, screen_height/2, 10, 100)
    elif mouse [0] < screen_width/2:
        opponent = pygame.Rect(screen_width-20, screen_height/2, 10, 100)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player2_speed += 3

                if event.key == pygame.K_UP:
                    player2_speed -= 3

                if event.key == pygame.K_w:
                    player1_speed -= 3

                if event.key == pygame.K_s:
                    player1_speed += 3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player2_speed += 3

                if event.key == pygame.K_DOWN:
                    player2_speed -= 3

                if event.key == pygame.K_w:
                    player1_speed += 3

                if event.key == pygame.K_s:
                    player1_speed -= 3


        player2_mov()
        ball_mov()
        if mouse[0] > screen_width/2:
            player1_mov()
        elif mouse[0] < screen_width/2:
            opponent_mov()

        screen2.fill(pygame.Color('#000000'))
        pygame.draw.ellipse(screen2, (255, 255, 255), ball)
        pygame.draw.rect(screen2, (255,31,0), player2)
        pygame.draw.line(screen2, (27, 35, 43), (screen_width / 2, 0), (screen_width / 2, screen_height), 5)
        if mouse[0] > screen_width / 2:
            pygame.draw.rect(screen2, (255, 31, 0), player1)
        if mouse[0] < screen_width / 2:
            pygame.draw.rect(screen2, (255,31,0), opponent)

        text = game_font.render("SCORE", False, (39, 255, 0))
        screen2.blit(text, (screen_width/2-77, 70))
        player2_text = game_font.render(f"{player2_score}", False, (255, 255, 255))
        screen2.blit(player2_text, (screen_width/2-52, 120))
        if mouse[0] > screen_width/2:
            player1_text = game_font.render(f"{player1_score}", False, (255, 255, 255))
            screen2.blit(player1_text, (screen_width/2+35, 120))
        if mouse[0] < screen_width/2:
            opponent_text = game_font.render(f"{opponent_score}", False, (255, 255, 255))
            screen2.blit(opponent_text, (screen_width/2+35, 120))

        pygame.display.flip()
        clock.tick(60)


mouse = pygame.mouse.get_pos()
font = pygame.font.SysFont("Times new Roman", 40)
while True:
    screen1.fill(pygame.Color('#000000'))
    for ev in pygame.event.get():
        if ev.type == pygame.MOUSEBUTTONUP:
            game()
            pygame.quit()
            sys.exit()

        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.line(screen1, (27, 35, 43), (screen_width/2,0),(screen_width/2, screen_height), 5)
    option1 = font.render("Play with CPU", False, (255, 23, 0))
    screen1.blit(option1, (screen_width / 4-100, screen_height / 2-50))
    option2 = font.render("Play with Player 2", False, (255, 23, 0))
    screen1.blit(option2, (3 * screen_width / 4-100 , screen_height / 2-50))

    pygame.display.flip()
