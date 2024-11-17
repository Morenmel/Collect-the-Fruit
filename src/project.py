import pygame


def main():
    pygame.init()
    pygame.display.set_caption("Collect the Fruit!")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()

    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game Logic


        # Render & Display
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()

