import pygame, sys
from game import Game
from colors import Colors
import os

pygame.init()


# Add the resource_path function
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215 - 50, 170, 180)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Stellar Stellar Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 500)

# Use the resource_path function for image and other asset paths
background_image = pygame.image.load(resource_path("Images/bg.jpg")).convert()
screen_width, screen_height = screen.get_size()
background_image = pygame.transform.scale(
    background_image, (screen_width, screen_height)
)

new_image_path = resource_path("Images/sui.jpg")
new_image = pygame.image.load(new_image_path).convert()
new_image = pygame.transform.scale(new_image, (next_rect.width, next_rect.height))
new_image_rect = new_image.get_rect(
    topleft=(320, 450 - 90 + game_over_surface.get_height() + 10)
)

move_delay = 50  # delay in milliseconds
last_move_time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_j and game.game_over == False:
                game.rotate()
            if event.key == pygame.K_SPACE and not game.game_over:
                game.hard_drop()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    keys = pygame.key.get_pressed()
    current_time = pygame.time.get_ticks()

    if game.game_over == False:
        if keys[pygame.K_a] and current_time - last_move_time > move_delay:
            game.move_left()
            last_move_time = current_time
        if keys[pygame.K_d] and current_time - last_move_time > move_delay:
            game.move_right()
            last_move_time = current_time
        if keys[pygame.K_s] and current_time - last_move_time > move_delay:
            game.move_down()
            last_move_time = current_time
            game.update_score(0, 1)

    # Drawing
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.blit(background_image, (0, 0))
    screen.blit(new_image, new_image_rect.topleft)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180 - 50, 50, 50))

    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450 - 90, 50, 50))
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(
        score_value_surface,
        score_value_surface.get_rect(
            centerx=score_rect.centerx, centery=score_rect.centery
        ),
    )
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
