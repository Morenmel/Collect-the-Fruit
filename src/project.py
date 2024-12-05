import pygame
from PIL import Image
import random


class PlayerObject(pygame.sprite.Sprite):
    def __init__(self, x=290, y=600, sprite_path='graphics/basket_object.png'):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, posX, posY):
        self.rect.x += posX
        self.rect.y += posY

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Fruit(pygame.sprite.Sprite):
    def __init__(self, x=15, y=15, center=15):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("graphics/apple_object.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.center = center

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class FallingFruit():
    def __init__(self, pos, size):
        self.image = pygame.image.load("graphics/apple_object.png").convert_alpha()
        self.angle1 = 0
        self.pos = pos
        self.size = size
        self.fruits = []
        self._update_pos()

    def update(self, dt):
        fruit = Fruit(self.pos, self.size)
        self.fruits.insert(0, fruit)
        self._update_pos()
    
    def _update_pos(self):
        x, y = self.pos
        y += self.size
        self.pos = (x, y)
        self.rect = (self.pos)

    def draw(self, surface):
        self.angle1 += 5
        rotate_img = pygame.transform.rotate(self.image, self.angle1)
        surface.blit(rotate_img, self.pos)


class Rain():
    def __init__(self, screen_res):
        self.screen_res = screen_res
        self.fruit_size = 13
        self.birth_rate = 1
        self.y = 0
        self.fruits = []

    def update(self, dt):
        self._birth_new_fruits()
        self._update_fruits(dt)

    def _update_fruits(self, dt):
        for idx, fruit in enumerate(self.fruits):
            fruit.update(dt)
            if self._fruit_on_ground(fruit):
                del self.fruits[idx]

    def _fruit_on_ground(self, fruit):
        fruit_on_ground = fruit.fruits[0].pos[1] > 672
        return fruit_on_ground
    
    def _birth_new_fruits(self):
        for num in range(self.birth_rate):
            x = random.randrange(115, 565)
            self.y -= 200
            pos = (x, self.y)
            fruit = FallingFruit(pos, self.fruit_size)
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

    font = pygame.font.SysFont("Arial", 25)
    score = 0
    text = f"Score: {score}"

    rain = Rain(resolution)

    with Image.open("graphics/new_basket.png") as img:
        resized = img.resize((124, 56))
        resized.save("graphics/basket_object.png")
    
    # Player img placeholder
    player = PlayerObject(x=290, y=600)
    fruit = Fruit(pos=(15, 15), center=15)

    player_group = pygame.sprite.Group(player)
    fruit_group = pygame.sprite.Group(fruit)

    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(posX= -18, posY = 0)
        if keys[pygame.K_RIGHT]:
            player.move(posX= 18, posY = 0)
        
        collision = pygame.sprite.collide_rect(player, fruit)
        if collision:
            print("COLLISION")
            score += 1

        # Game Logic
        rain.update(dt)


        # Render & Display
        sky_blue = pygame.Color(133, 212, 255)
        green = pygame.Color(36, 128, 43)

        # sky background
        screen.fill(sky_blue)

        # tree trunk
        tree_trunk = pygame.image.load("graphics/tree_trunk.png").convert_alpha()
        screen.blit(tree_trunk, (0, 0))

        # ground
        surf = pygame.Surface((800, 100))
        surf.fill(green)
        screen.blit(surf, (0, 700))

        # apples
        rain.draw(screen)

        # player
        player.draw(screen)

        # tree leaves
        tree_leaves = pygame.image.load("graphics/tree_leaves.png").convert_alpha()
        screen.blit(tree_leaves, (0, 0))

        # score text
        score_text = font.render(text, True, (0, 0, 0))
        screen.blit(score_text, (10, 760))

        dt = clock.tick(18)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()

