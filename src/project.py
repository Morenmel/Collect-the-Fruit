import pygame
from PIL import Image
import random


class PlayerObject():
    def __init__(self, pos=(0,0), sprite_path=''):
        self.pos = pygame.Vector2(pos)
        self.speed = 15
        self.image = pygame.image.load(sprite_path).convert_alpha()

    def move(self, direction):
        self.pos = self.pos + direction * self.speed
    
    def draw(self, screen):
        screen.blit(self.image, self.pos)


class Fruit():
    def __init__(self, pos=(15, 15), center=15, life=1000):
        self.pos = pos
        self.center = center
        self.life = life
        self.color = pygame.Color(255, 0, 0)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.center)


class FallingFruit():
    def __init__(self, pos, size, life):
        self.pos = pos
        self.size = size
        self.life = life
        self.fruits = []
        self._update_pos()

    def update(self, dt):
        fruit = Fruit(self.pos, self.size, self.life)
        self.fruits.insert(0, fruit)
        self._update_pos()
    
    def _update_pos(self):
        x, y = self.pos
        y += self.size
        self.pos = (x, y)

    def draw(self, surface):
        for fruit in self.fruits:
            fruit.draw(surface)


def main():
    pygame.init()
    pygame.display.set_caption("Collect the Fruit!")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()
    dt = 0

    #fruit = Fruit()
    falling = FallingFruit((15, 0), 15, 1000)

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
        falling.update(dt)


        # Render & Display
        black = pygame.Color(0, 0, 0)
        green = pygame.Color(36, 128, 43)

        screen.fill(black)
        surf = pygame.Surface((800, 100))
        surf.fill(green)
        screen.blit(surf, (0, 540))

        falling.draw(screen)

        clock.tick(12)
        player.draw(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()

