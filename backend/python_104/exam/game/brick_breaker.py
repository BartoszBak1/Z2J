import pygame
class ScreenSize():
    def __init__(self) -> None:
        self.screen_height = 300
        self.screen_wight = 400

class Ball(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        ScreenSize.__init__(self)
        self.radius = 5
        self.color = (255, 255, 255)
        self.step = 2
        self.x_direction = 1
        self.y_direction = 1
        self.image = pygame.Surface((2*self.radius, 2*self.radius))
        self.image.fill("black")
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center = ( self.screen_wight//2 ,self.screen_height*0.1))

    def move(self, direction):
        self.rect.x += self.step
        self.rect.y += self.step

    def wall_collision(self):
        if self.rect.x <= self.radius:
            self.x_direction = 1
        if self.rect.x >= self.screen_wight - self.radius:
            self.x_direction = -1
        if self.rect.y <= self.radius:
            self.y_direction = 1    

    def update(self):
        self.rect.x += self.step * self.x_direction
        self.rect.y += self.step * self.y_direction

    
class Racket(pygame.sprite.Sprite, ScreenSize):
    def __init__(self) -> None:
        super().__init__()
        ScreenSize.__init__(self)
        self.width = 60
        self.height = 10
        self.color = (255, 255, 255)
        self.step = 10
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("black")
        pygame.draw.rect(self.image, self.color, (0, 0, self.width, self.height))
        self.rect = self.image.get_rect(bottomleft = (0, self.screen_height-20))

    def move(self):
        keys = pygame.key.get_pressed()
        
        # warunki do zmiany pozycji obiektu
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.step
        if keys[pygame.K_RIGHT] and self.rect.right < self.screen_wight:
            self.rect.x += self.step
            return

    def update(self):
        self.move()


class Brick(pygame.sprite.Sprite):
    def __init__(self, width = 40, height = 10, color = (0, 255, 0)) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("black")
        pygame.draw.rect(self.image, self.color, (0, 0, self.width, self.height))
        self.rect = self.image.get_rect()

        # topleft = (0, 0)    # 