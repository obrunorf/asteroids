from constants import *
from circleshape import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0
        self.original_image = pygame.image.load("spaceship.png").convert_alpha()
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x,y))

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        #pygame.draw.polygon(screen, 'white', self.triangle(), 2)
        screen.blit(self.image, self.rect)

    def rotate(self, dt):
        self.rotation = self.rotation + PLAYER_STEERING * dt
        self.image = pygame.transform.rotate(self.original_image, -self.rotation)
        self.rect = self.image.get_rect(center=self.position)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        self.rect = self.image.get_rect(center=self.position)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate( - dt)
        if keys[pygame.K_d]:
            self.rotate( dt )
        if keys[pygame.K_w]:
            self.move( dt )
        if keys[pygame.K_s]:
            self.move( - dt )
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS) #creates bullet at current position
        bullet.velocity = PLAYER_SHOT_SPEED * pygame.Vector2(0, 1).rotate(self.rotation)