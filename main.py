from os.path import join
from pytmx.util_pygame import load_pygame
from settings import *



class Game:
    def __int__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("British Simulator")
        self.clock = pygame.time.Clock()

        self.tmx_maps = {0: load_pygame(join("/PirateGame/PirateGame/ImportantStuff", "data", "levels", "omni.tmx"))}
        print(self.tmx_maps)

        self.current_stage = Level(self.tmx_maps[0])


    def run(self):
        while True:
            dt = self.clock.tick(30) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.current_stage.run(dt)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()