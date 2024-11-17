import pygame
from PIL import Image

class GameObject:
    def __init__(self, pos=(0,0), sprite_path=''):
        self.pos = pygame.Vector2(pos)
        self.speed = 3.0
        self.image = pygame.image.load(sprite_path).convert_alpha()

    def move(self, direction):
        self.pos = self.pos + direction * self.speed
    
    def draw(self, screen):
        screen.blit(self.image, self.pos)

def main():
    pygame.init()
    pygame.display.set_caption("Collect the Fruit!")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()

    with Image.open("graphics/apple.png") as img:
        resized = img.resize((70, 65))
        resized.save("graphics/apple_object.png")
    
    player = GameObject(pos=((320, 240)), sprite_path="graphics/apple_object.png")

    running = True
    keys = pygame.key.get_pressed()
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if keys[pygame.K_LEFT]:
            player.move(pygame.Vector2(-1, 0))
        if keys[pygame.K_RIGHT]:
            player.move(pygame.Vector2(1, 0))

        # Game Logic


        # Render & Display
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()

