import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
  print("Starting asteroids!")
  pygame.init()
  clock = pygame.time.Clock()
  dt = 0
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  Player.containers = (updatable, drawable)
  Asteroid.containers = (updatable, drawable, asteroids)
  Shot.containers = (updatable, drawable, shots)
  AsteroidField.containers = (updatable)
  asteroidfield = AsteroidField()
  player = Player(x, y)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    for item in updatable:
      item.update(dt)

    screen.fill("black")
    
    for item in drawable:
      item.draw(screen)    
    
    for asteroid in asteroids:
      if player.collides_with(asteroid):
        print("Game over!")
        exit()
      for shot in shots:
         if pygame.math.Vector2.distance_to(asteroid.position, shot.position) <= (asteroid.radius + shot.radius):
           asteroid.split()
           shot.kill() 
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000


if __name__ == "__main__":
  main()
