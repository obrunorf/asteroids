from circleshape import *
from constants import *
from random import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
                         
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position , self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        angle = uniform(20,50)
        x= self.position.x
        y= self.position.y
        a1 = Asteroid(x,y, new_radius)
        a2 = Asteroid(x,y, new_radius)
        a1.velocity = self.velocity * 1.2
        a1.velocity = a1.velocity.rotate(angle)
        a2.velocity = self.velocity * 1.2
        a2.velocity = a2.velocity.rotate(-angle)

        self.kill()