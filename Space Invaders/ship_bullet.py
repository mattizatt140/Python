from bullet import Bullet

class Ship_Bullet(Bullet):
    """A subclass of Bullet used exclusively for ship bullets"""

    def __init__(self, ai_settings, screen, ship):
        """Construct ship bullet"""
        # Construct super class
        super().__init__(ai_settings, screen)

        # Move bullet to the location of ship
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        # Give ship bullet unique color and speed
        self.color = ai_settings.ship_bullet_color
        self.speed_factor = ai_settings.ship_bullet_speed_factor

    def update(self):
        """Move the ship bullet up the screen"""
        # Adjust y-coordinate position
        self.y -= self.speed_factor 

        # Set rect position equal to y position
        self.rect.y = self.y