import pygame
from tetris import Tetris
from draw import draw_figure, draw_screen, draw_gameover, draw_score, draw_title, draw_any_key, on_keypress

#make speed start slower, speed up as time/score increases
#next blocks
#save block with shift


if __name__ == "__main__":
    # Initialize the game engine
    pygame.init()

    # Define some colors
    size = (400, 500)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Tetris")

    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()
    fps = 25
    game = Tetris(20, 10)
    counter = 0
    pressing_down = False

    while not done:
        draw_title(screen)
        
        draw_screen(game, screen)
        
        if game.state == "false":
            draw_any_key(screen)

        pressing_down, done = on_keypress(game, pressing_down, done, screen)

        if game.state == "start":

            if game.figure is None:
                game.new_figure()

            counter += 1
            if counter > 100000:
                counter = 0
            
            if counter % ((fps // game.level) // 2) == 0 or pressing_down:
                game.go_down()

            draw_figure(game, screen)
            draw_score(game, screen)
            draw_title(screen)  
        if game.state == "gameover":
            draw_gameover(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
