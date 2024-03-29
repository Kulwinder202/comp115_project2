import sys
import pygame
class AlienInvasion:
 """Overall class to manage game assets and behavior."""
 def __init__(self):
   """Initialize the game, and create game resources."""
   pygame.init()
   self.screen = pygame.display.set_mode((1200, 800))
   pygame.display.set_caption("Alien Invasion")
 def run_game(self):
  """Start the main loop for the game."""
  while True:
     # Watch for keyboard and mouse events.
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
     # Make the most recently drawn screen visible.
    pygame.display.flip()
  if __name__ == '__main__':
      # Make a game instance, and run the game. 
      ai = AlienInvasion()
      ai.run_game()
def __init__(self):
      """Initialize the game, and create game resources."""
      pygame.init()
      self.clock = pygame.time.Clock()
    
def run_game(self):
    """Start the main loop for the game."""
    while True:
     
       pygame.display.flip()
       self.clock.tick(60)
def __init__(self):
    
    pygame.display.set_caption("Alien Invasion")
    # Set the background color.
    self.bg_color = (230, 230, 230)
def run_game(self):
    
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
      # Redraw the screen during each pass through the loop.
      self.screen.fill(self.bg_color)
      # Make the most recently drawn screen visible.
      pygame.display.flip()
      self.clock.tick(60)
class Settings:
  """A class to store all settings for Alien Invasion."""
  def __init__(self):
     """Initialize the game's settings."""
     # Screen settings
     self.screen_width = 1200
     self.screen_height = 800
     self.bg_color = (230, 230, 230)


import pygame
from settings import Settings
class AlienInvasion:
  """Overall class to manage game assets and behavior."""
  def __init__(self):
     """Initialize the game, and create game resources."""
     pygame.init()
     self.clock = pygame.time.Clock()
     self.settings = Settings()
     self.screen = pygame.display.set_mode(
        (self.settings.screen_width, self.settings.screen_height))
     pygame.display.set_caption("Alien Invasion") 
  def run_game(self):
    
     # Redraw the screen during each pass through the loop.
     self.screen.fill(self.settings.bg_color)
     # Make the most recently drawn screen visible.
     pygame.display.flip()
     self.clock.tick(60)
     

class Ship:
  """A class to manage the ship."""
  def __init__(self, ai_game):
   """Initialize the ship and set its starting position."""
   self.screen = ai_game.screen
   self.screen_rect = ai_game.screen.get_rect()
   # Load the ship image and get its rect.
   self.image = pygame.image.load('images/ship.bmp')
   self.rect = self.image.get_rect()
   # Start each new ship at the bottom center of the screen.
   self.rect.midbottom = self.screen_rect.midbottom
  def blitme(self):
   """Draw the ship at its current location."""
   self.screen.blit(self.image, self.rect)

from settings import Settings
from ship import Ship
class AlienInvasion:
  """Overall class to manage game assets and behavior."""
  def __init__(self):
     
     pygame.display.set_caption("Alien Invasion")
     self.ship = Ship(self)
  def run_game(self):
    
     # Redraw the screen during each pass through the loop.
     self.screen.fill(self.settings.bg_color)
     self.ship.blitme()
     # Make the most recently drawn screen visible.
     pygame.display.flip()
     self.clock.tick(60)

class Ship:
 """A class to manage the ship."""
  def __init__(self, ai_game):
 """Initialize the ship and set its starting position."""
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()
 # Load the ship image and get its rect.
    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()
 # Start each new ship at the bottom center of the screen.
    self.rect.midbottom = self.screen_rect.midbottom
  def blitme(self):
 """Draw the ship at its current location."""
    self.screen.blit(self.image, self.rect)
    from settings import Settings
from ship import Ship

class AlienInvasion:
 """Overall class to manage game assets and behavior."""
 def __init__(self):
 --snip--
 pygame.display.set_caption("Alien Invasion")
1 self.ship = Ship(self)
 def run_game(self):
 --snip--
 # Redraw the screen during each pass through the loop.
 self.screen.fill(self.settings.bg_color)
2 self.ship.blitme()
 # Make the most recently drawn screen visible.
 pygame.display.flip()
 self.clock.tick(60)

  def run_game(self):
 """Start the main loop for the game."""
 while True:
1 self._check_events()
 # Redraw the screen during each pass through the loop.
 --snip--
2 def _check_events(self):
 """Respond to keypresses and mouse events."""
 for event in pygame.event.get():
 if event.type == pygame.QUIT:
 sys.exit()
 def run_game(self):
 """Start the main loop for the game."""
 while True:
 self._check_events()
 self._update_screen()
 self.clock.tick(60)
 def _check_events(self):
  def _update_screen(self):
 """Update images on the screen, and flip to the new screen."""
 self.screen.fill(self.settings.bg_color)
 self.ship.blitme()
 pygame.display.flip()
 def _check_events(self):
 """Respond to keypresses and mouse events."""
 for event in pygame.event.get():
 if event.type == pygame.QUIT:
 sys.exit()
1 elif event.type == pygame.KEYDOWN:
2 if event.key == pygame.K_RIGHT:
 # Move the ship to the right.
3 self.ship.rect.x += 1
class Ship:
 """A class to manage the ship."""
 def __init__(self, ai_game):
 --snip--
 # Start each new ship at the bottom center of the screen.
 self.rect.midbottom = self.screen_rect.midbottom

 # Movement flag; start with a ship that's not moving.
1 self.moving_right = False
2 def update(self):
 """Update the ship's position based on the movement flag."""
 if self.moving_right:
 self.rect.x += 1
 def blitme(self):
  def _check_events(self):
 """Respond to keypresses and mouse events."""
 for event in pygame.event.get():
 --snip--
 elif event.type == pygame.KEYDOWN:
 if event.key == pygame.K_RIGHT:
1 self.ship.moving_right = True
2 elif event.type == pygame.KEYUP:
 if event.key == pygame.K_RIGHT:
 self.ship.moving_right = False
 def run_game(self):
 """Start the main loop for the game."""
 while True:
 self._check_events()
 self.ship.update()
 self._update_screen()
 self.clock.tick(60)
 def __init__(self, ai_game):
 --snip--
 # Movement flags; start with a ship that's not moving.
 self.moving_right = False
 self.moving_left = False
 def update(self):
 """Update the ship's position based on movement flags."""
 if self.moving_right:
 self.rect.x += 1
 if self.moving_left:
 self.rect.x -= 1
 def _check_events(self):
 """Respond to keypresses and mouse events."""
 for event in pygame.event.get():
 --snip--
 elif event.type == pygame.KEYDOWN:
 if event.key == pygame.K_RIGHT:
 self.ship.moving_right = True
 elif event.key == pygame.K_LEFT:
 self.ship.moving_left = True
 elif event.type == pygame.KEYUP:
 if event.key == pygame.K_RIGHT:
 self.ship.moving_right = False
 elif event.key == pygame.K_LEFT:
 self.ship.moving_left = False
 class Settings:
 """A class to store all settings for Alien Invasion."""
 def __init__(self):
 --snip--
 # Ship settings
 self.ship_speed = 1.5
 class Ship:
 """A class to manage the ship."""
 def __init__(self, ai_game):
 """Initialize the ship and set its starting position."""
 self.screen = ai_game.screen
1 self.settings = ai_game.settings
 --snip--
 # Start each new ship at the bottom center of the screen.
 self.rect.midbottom = self.screen_rect.midbottom
 # Store a float for the ship's exact horizontal position.
2 self.x = float(self.rect.x)
 # Movement flags; start with a ship that's not moving.
 self.moving_right = False
 self.moving_left = False
 def update(self):
 """Update the ship's position based on movement flags."""
 # Update the ship's x value, not the rect.
 if self.moving_right:
3 self.x += self.settings.ship_speed
A Ship That Fires Bullets   243
 if self.moving_left:
 self.x -= self.settings.ship_speed
 # Update rect object from self.x.
4 self.rect.x = self.x
 def blitme(self):
  def update(self):
 """Update the ship's position based on movement flags."""
 # Update the ship's x value, not the rect.
1 if self.moving_right and self.rect.right < self.screen_rect.right:
 self.x += self.settings.ship_speed
2 if self.moving_left and self.rect.left > 0:
 self.x -= self.settings.ship_speed
 # Update rect object from self.x.
 self.rect.x = self.x
 def _check_events(self):
 """Respond to keypresses and mouse events."""
 for event in pygame.event.get():
 if event.type == pygame.QUIT:
 sys.exit()
 elif event.type == pygame.KEYDOWN:
 self._check_keydown_events(event)
 elif event.type == pygame.KEYUP:
 self._check_keyup_events(event)
 def _check_keydown_events(self, event):
 """Respond to keypresses."""
 if event.key == pygame.K_RIGHT:
 self.ship.moving_right = True
 elif event.key == pygame.K_LEFT:
 self.ship.moving_left = True
 def _check_keyup_events(self, event):
 """Respond to key releases."""
 if event.key == pygame.K_RIGHT:
 self.ship.moving_right = False
 elif event.key == pygame.K_LEFT:
 self.ship.moving_left = False
 def _check_keydown_events(self, event):
 --snip--
 elif event.key == pygame.K_LEFT:
A Ship That Fires Bullets   245
 self.ship.moving_left = True
 elif event.key == pygame.K_q:
 sys.exit()
 def __init__(self):
 """Initialize the game, and create game resources."""
 pygame.init()
 self.settings = Settings()
1 self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
2 self.settings.screen_width = self.screen.get_rect().width
 self.settings.screen_height = self.screen.get_rect().height
 pygame.display.set_caption("Alien Invasion")
 class Bullet(Sprite):
 """A class to manage bullets fired from the ship."""
 def __init__(self, ai_game):
 """Create a bullet object at the ship's current position."""
 super().__init__()
 self.screen = ai_game.screen
 self.settings = ai_game.settings
 self.color = self.settings.bullet_color
 # Create a bullet rect at (0, 0) and then set correct position.
1 self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
 self.settings.bullet_height)
2 self.rect.midtop = ai_game.ship.rect.midtop
 # Store the bullet's position as a float.
3 self.y = float(self.rect.y)
def update(self):
 """Move the bullet up the screen."""
 # Update the exact position of the bullet.
1 self.y -= self.settings.bullet_speed
 # Update the rect position.
2 self.rect.y = self.y
 def draw_bullet(self):
 """Draw the bullet to the screen."""
3 pygame.draw.rect(self.screen, self.color, self.rect)
 def _check_keydown_events(self, event):
 --snip--
 elif event.key == pygame.K_q:
 sys.exit()
1 elif event.key == pygame.K_SPACE:
 self._fire_bullet()
 def _check_keyup_events(self, event):
 --snip--
 def _fire_bullet(self):
 """Create a new bullet and add it to the bullets group."""
2 new_bullet = Bullet(self)
3 self.bullets.add(new_bullet)
250   Chapter 12
 def _update_screen(self):
 """Update images on the screen, and flip to the new screen."""
 self.screen.fill(self.settings.bg_color)
4 for bullet in self.bullets.sprites():
 bullet.draw_bullet()
 self.ship.blitme()
 pygame.display.flip()
 def run_game(self):
 """Start the main loop for the game."""
 while True:
 self._check_events()
 self.ship.update()
 self.bullets.update()
 # Get rid of bullets that have disappeared.
1 for bullet in self.bullets.copy():
2 if bullet.rect.bottom <= 0:
3 self.bullets.remove(bullet)
4 print(len(self.bullets))
 self._update_screen()
 self.clock.tick(60)
 def _fire_bullet(self):
 """Create a new bullet and add it to the bullets group."""
 if len(self.bullets) < self.settings.bullets_allowed:
 new_bullet = Bullet(self)
 self.bullets.add(new_bullet)
 def _update_bullets(self):
 """Update position of bullets and get rid of old bullets."""
 # Update bullet positions.
 self.bullets.update()
 # Get rid of bullets that have disappeared.
 for bullet in self.bullets.copy():
 if bullet.rect.bottom <= 0:
 self.bullets.remove(bullet)
 while True:
 self._check_events()
 self.ship.update()
 self._update_bullets()
 self._update_screen()
 self.clock.tick(60)