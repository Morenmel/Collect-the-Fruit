import pygame
from PIL import Image
import random


class PlayerObject():
    def __init__(self, pos=(0,0), sprite_path=''):
        self.pos = pygame.Vector2(pos)
        self.speed = 18
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
    def __init__(self, pos, size, life, sprite_path="graphics/apple_object.png"):
        self.pos = pos
        self.size = size
        self.life = life
        self.color = pygame.Color(255, 0, 0)
        self.image = pygame.image.load(sprite_path).convert_alpha()
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
        #pygame.draw.circle(surface, self.color, self.pos, self.size)
        surface.blit(self.image, self.pos)


class Rain():
    def __init__(self, screen_res):
        self.screen_res = screen_res
        self.fruit_size = 15
        self.birth_rate = 1
        self.fruits = []

    def update(self, dt):
        self._birth_new_fruits()
        self._update_fruits(dt)

    def _update_fruits(self, dt):
        for idx, fruit in enumerate(self.fruits):
            fruit.update(dt)
            if self._offscreen_fruit(fruit):
                print("deleting fruit...")
                del self.fruits[idx]

    def _offscreen_fruit(self, fruit):
        offscreen_fruit = fruit.fruits[0].pos[1] > self.screen_res[1]
        return offscreen_fruit
    
    def _birth_new_fruits(self):
        for num in range(self.birth_rate):
            screen_width = self.screen_res[0]
            x = random.randrange(100, screen_width, self.fruit_size)
            pos = (x, -50)
            life = random.randrange(100, 500)
            fruit = FallingFruit(pos, self.fruit_size, life)
            self.fruits.insert(0, fruit)

    def draw(self, surface):
        for fruit in self.fruits:
            fruit.draw(surface)


def main():
    pygame.init()
    pygame.display.set_caption("Collect the Fruit!")
    resolution = (705, 800)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()
    dt = 0

    #fruit = Fruit()
    #falling = FallingFruit((15, 0), 15, 1000)
    rain = Rain(resolution)

    with Image.open("graphics/basket.png") as img:
        resized = img.resize((124, 56))
        resized.save("graphics/basket_object.png")
    
    # Player img placeholder
    player = PlayerObject(pos=((100, 610)), sprite_path="graphics/basket_object.png")

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
        rain.update(dt)


        # Render & Display
        black = pygame.Color(0, 0, 0)
        sky_blue = pygame.Color(129, 190, 235)
        green = pygame.Color(36, 128, 43)

        screen.fill(sky_blue)
        surf = pygame.Surface((800, 100))
        surf.fill(green)
        screen.blit(surf, (0, 700))

        rain.draw(screen)

        clock.tick(12)
        player.draw(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()

