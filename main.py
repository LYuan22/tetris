import pygame
from tetris import Tetris


#make speed start slower, speed up as time/score increases
#keypress
#next blocks
#save block with shift
#move things to functions

#press any key to start

def draw_figure(game):
    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    pygame.draw.rect(screen, colors[game.figure.color],
                                   [game.x + game.zoom * (j + game.figure.x) + 1,
                                    game.y + game.zoom * (i + game.figure.y) + 1,
                                    game.zoom - 2, game.zoom - 2])

def draw_screen(game):
    screen.fill(WHITE)
    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colors[game.field[i][j]],
                            [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

def draw_gameover():
    font = pygame.font.SysFont('Calibri', 65, True, False)
    text_game_over = font.render("Game Over", True, BLACK)
    text_game_over1 = font.render("Press ESC", True, BLACK)
    
    screen.blit(text_game_over, [20, 200])
    screen.blit(text_game_over1, [25, 265])

def draw_score(game):
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Score: " + str(game.score), True, BLACK)
    screen.blit(text, [2, 2])

def draw_title():
    font = pygame.font.SysFont('Calibri', 40, True, False)
    text_TETRIS = font.render("TETRIS", True, BLACK)

    screen.blit(text_TETRIS, [137, 20])


def on_keypress(game, pressing_down, done):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                game.go_side(-1)
            if event.key == pygame.K_RIGHT:
                game.go_side(1)
            if event.key == pygame.K_SPACE:
                if game.state == "start":
                    game.go_space()
            if event.key == pygame.K_ESCAPE:
                if game.state == "gameover":
                    game.__init__(20, 10)

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pressing_down = False
    return pressing_down, done


if __name__ == "__main__":
    # Initialize the game engine
    pygame.init()

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)

    colors = [
    (0, 0, 0),
    (0, 255, 255),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 128, 0),
    (128, 0, 128),
    (255, 255, 0)] 

    size = (400, 500)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Tetris")

    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()
    fps = 25
    game = Tetris(20, 10)
    counter = 5000
    pressing_down = False

    while not done:
        draw_title
        if game.figure is None:
            game.new_figure()
        counter += 1
        if counter > 100000:
            counter = 0

        if counter % ((fps // game.level) // 2) == 0 or pressing_down:
            if game.state == "start":
                game.go_down()

        pressing_down, done = on_keypress(game, pressing_down, done)
        #draws screen and box
        draw_screen(game)  
        #draws figures
        draw_figure(game)
        draw_score(game)
        if game.state == "gameover":
            draw_gameover()
        draw_title()  
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
