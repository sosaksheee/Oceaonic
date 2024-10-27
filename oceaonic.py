import pygame
import random

# Initialize pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 105, 148)
FPS = 60

# Load assets
AVATAR_IMG = pygame.image.load('avatar.png')  # Add an image for the Guardian character
OCEAN_BG = pygame.image.load('ocean_bg.jpg')  # Background image of the ocean

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ocean Odyssey: Guardians of the Deep')

# Player (Guardian) class
class Guardian:
    def __init__(self, x, y):
        self.image = AVATAR_IMG
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5

    def move(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT] and self.rect.x - self.speed > 0:  # Move left
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT] and self.rect.x + self.speed + self.rect.width < SCREEN_WIDTH:  # Move right
            self.rect.x += self.speed
        if keys_pressed[pygame.K_UP] and self.rect.y - self.speed > 0:  # Move up
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_DOWN] and self.rect.y + self.speed + self.rect.height < SCREEN_HEIGHT:  # Move down
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Object to interact with (like ocean creatures, challenges, etc.)
class OceanObject:
    def __init__(self):
        self.image = pygame.image.load('fish.png')  # Example: fish or trash
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Main game loop
def main():
    clock = pygame.time.Clock()
    guardian = Guardian(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    ocean_objects = [OceanObject() for _ in range(5)]  # Add multiple interactive objects

    running = True
    while running:
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()

        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update Guardian movement
        guardian.move(keys_pressed)

        # Render the game
        screen.blit(OCEAN_BG, (0, 0))  # Draw background
        guardian.draw(screen)  # Draw the player character
        for obj in ocean_objects:
            obj.draw(screen)  # Draw objects in the ocean

        # Update display
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()

