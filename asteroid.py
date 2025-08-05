import pygame, random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-ASTEROID_ROTATION_SPEED, ASTEROID_ROTATION_SPEED)
        self.num_sides = random.randint(ASTEROID_MIN_SIDES, ASTEROID_MAX_SIDES)  # Random number of sides for the asteroid
        self.point_offsets = []
        for i in range(self.num_sides):
            # Randomly adjust the radius for each vertex to create an irregular shape
            offset = random.uniform(-radius * 0.2, radius * 0.2)
            self.point_offsets.append(offset)

    def asteroid_shape(self):
        poly_points = []
        for i in range(self.num_sides):
            angle = i * (360 / self.num_sides) + self.rotation
            # Calculate the point on the asteroid's circumference based on the angle and radius
            point = pygame.Vector2(0, self.radius + self.point_offsets[i]).rotate(angle)
            poly_points.append(self.position + point)
        return poly_points

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.asteroid_shape(), 2)

    def update(self, dt):
        if self.position.x < -self.radius*2 or self.position.x > SCREEN_WIDTH + self.radius*2 or \
           self.position.y < -self.radius*2 or self.position.y > SCREEN_HEIGHT + self.radius*2:
            self.kill()
        else:
            self.position += self.velocity * dt
            self.rotation += self.rotation_speed * dt

    def split(self):
        # Split the asteroid into smaller pieces
        self.kill()  # Remove the current asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            # Create two smaller asteroids with the new angle and radius
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = self.velocity.rotate(new_angle) * random.uniform(1, ASTEROID_MAX_SPEED_CHANGE)
            asteroid2.velocity = self.velocity.rotate(-new_angle) * random.uniform(1, ASTEROID_MAX_SPEED_CHANGE)

