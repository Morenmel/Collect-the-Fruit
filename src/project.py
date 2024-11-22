import pygame
from PIL import Image


class PlayerObject:
    def __init__(self, pos=(0,0), sprite_path=''):
        self.pos = pygame.Vector2(pos)
        self.speed = 3.0
        self.image = pygame.image.load(sprite_path).convert_alpha()

    def move(self, direction):
        self.pos = self.pos + direction * self.speed
    
    def draw(self, screen):
        screen.blit(self.image, self.pos)


class Fruit:
    def __init__(self, pos=(15, 15), center=15):
        self.pos = pos
        self.center = center
        self.color = pygame.Color(255, 0, 0)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.center)


def main():
    pygame.init()
    pygame.display.set_caption("Collect the Fruit!")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()
    dt = 0

    fruit = Fruit()

    with Image.open("graphics/apple.png") as img:
        resized = img.resize((42, 37))
        resized.save("graphics/apple_object.png")
    
    # Player img placeholder
    player = PlayerObject(pos=((100, 480)), sprite_path="graphics/apple_object.png")

    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(pygame.Vector2(-1, 0))
        if keys[pygame.K_RIGHT]:
            player.move(pygame.Vector2(1, 0))

        # Game Logic


        # Render & Display
        black = pygame.Color(0, 0, 0)
        green = pygame.Color(36, 128, 43)

        screen.fill(black)
        surf = pygame.Surface((800, 100))
        surf.fill(green)
        screen.blit(surf, (0, 540))

        fruit.draw(screen)

        clock.tick(60)
        player.draw(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()

