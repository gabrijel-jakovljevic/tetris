import pygame
import sys
from game import Game
from colors import Colors

# --------------------------------------- Setup faza -------------------------------------------------------------------

pygame.init()

title_font = pygame.font.Font(None, 40)
text_font = pygame.font.Font(None, 28)
score_surface = title_font.render("Rezultat", True, Colors.white)
next_surface = title_font.render("Sljedeći", True, Colors.white)
game_over_surface = title_font.render("Kraj igre", True, Colors.red)

inputs_surface = title_font.render("Kontrole:", True, Colors.white)
up_surface = text_font.render("GORE - ispusti", True, Colors.white)
down_surface = text_font.render("DOLJE - dolje", True, Colors.white)
left_surface = text_font.render("LIJEVO - lijevo", True, Colors.white)
right_surface = text_font.render("DESNO - desno", True, Colors.white)

rotate_surface = text_font.render("X - rotiraj", True, Colors.white)
mirror_surface = text_font.render("C - zrcali", True, Colors.white)
space_surface = text_font.render("SPACE - kraj", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500, 770))
pygame.display.set_caption("Moj Tetris")

clock = pygame.time.Clock()
game = Game()

GAME_UPDATE = pygame.USEREVENT

speed = 500

pygame.time.set_timer(GAME_UPDATE, speed)

pygame.key.set_repeat(200, 50)

# --------------------------------------- Glavna petlja ----------------------------------------------------------------
while True:
    if game.progress_game:
        speed //= 1.25
        pygame.time.set_timer(GAME_UPDATE, int(speed))
        game.progress_game = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if game.game_over:
                game.game_over = False
                game.reset()
                speed = 500
                break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game.game_over:
                game.game_over = True
                game.reset()
                break
            if event.key == pygame.K_LEFT and not game.game_over:
                game.move_left()
            if event.key == pygame.K_RIGHT and not game.game_over:
                game.move_right()
            if event.key == pygame.K_DOWN and not game.game_over:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and not game.game_over:
                game.fall()
                game.update_score(0, 5)
            if event.key == pygame.K_x and not game.game_over:
                game.rotate()
            if event.key == pygame.K_c and not game.game_over:
                game.mirror()
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()

    # Crtanje
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (350, 20, 50, 50))
    screen.blit(next_surface, (350, 180, 50, 50))
    screen.blit(inputs_surface, (320, 430, 50, 50))
    screen.blit(up_surface, (320, 470, 50, 50))
    screen.blit(down_surface, (320, 500, 50, 50))
    screen.blit(left_surface, (320, 530, 50, 50))
    screen.blit(right_surface, (320, 560, 50, 50))
    screen.blit(rotate_surface, (320, 590, 50, 50))
    screen.blit(mirror_surface, (320, 620, 50, 50))
    screen.blit(space_surface, (320, 650, 50, 50))

    if game.game_over:
        screen.blit(game_over_surface, (350, 700, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx,
                                                                  centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)

# --------------------------------------- Testovi i misc ---------------------------------------------------------------

# -- Grid color-value test --
# game_grid.grid[0][0] = 1
# game_grid.grid[3][5] = 4
# game_grid.grid[17][8] = 3

# game_grid.print_grid()


# ----- Crtanje blokova test -----
# game_grid = Grid()  # grid objekt; vidi grid.py

# block = LBlock()
# block.move(11, 3)
